def run_setup_py_impl(ctx):
    installed_files = ctx.outputs.installed_files
    setup_py = [f for f in ctx.files.dep if f.path.endswith('/setup.py')][0]
    python_path = [f for f in ctx.files.deps if f.path.endswith('/python3')][0]
    commands = [
        'cd $(pwd)',
        'export DIR=$(pwd)/%s' % installed_files.dirname,
        'export PYTHON=$(pwd)/%s' % python_path.path,
        'export PATH=$(pwd)/$(dirname %s)/:$PATH' % python_path.path,
        'export LD_LIBRARY_PATH=$(pwd)/$(dirname %s)/../lib' %
        python_path.path,
        'export PYTHONHOME=$(pwd)/$(dirname %s)/../' % python_path.path,
        'export PYTHONPATH=$DIR', 'export PYTHONNOUSERSITE=true',
        'pushd %s > /dev/null' % setup_py.dirname,
        '$PYTHON setup.py install --home=$DIR --install-purelib=$DIR'
        + ' --install-platlib=$DIR --install-scripts=$DIR > /dev/null',
        'popd > /dev/null',
        'find $DIR | grep "^.*\.egg\$" > %s' % installed_files.path
    ]
    ctx.actions.run_shell(
        inputs=ctx.files.dep + ctx.files.deps,
        command=' && '.join(commands),
        mnemonic='RunPySetup',
        outputs=[installed_files],
        env=dict())

run_setup_py = rule(
    run_setup_py_impl,
    attrs = {
        "dep": attr.label(allow_files = True),
        "deps": attr.label_list(allow_files = True),
        "installed_files": attr.output(),
    },
)

def python_package_lib(name, dep, **kwargs):
    # Install the files into the current directory and save them into a file.
    run_setup_py(
        name=name + '_build_files',
        installed_files=name + '_eggs',
        dep=dep,
        deps=["//tools:python_3_6"], )

    # Can't add eggs into runfiles so just create a loader module that
    # hacks sys.path with the eggs generated by setup.py.
    src = ':' + name + '_build_files'
    commands = [
        'echo "import sys" > $@',
        'export FILES=$(locations %s)' % src, 'for l in $$(cat $$FILES); do ' +
        'echo "sys.path.append(\'$$l\')" >> $@; done'
    ]
    native.genrule(
        name=name + '_loader',
        outs=[name + '_loader.py'],
        srcs=[src],
        cmd=' && '.join(commands))
    native.py_library(name=name, srcs=[':' + name + '_loader'], **kwargs)

def python_package_bundle(name, deps, visibility=None):
    lib_deps = []
    modules = []
    for idx, dep in enumerate(deps):
        base_name = '%s_%d_dep' % (name, idx)
        python_package_lib(base_name, dep)
        lib_deps = lib_deps + [':' + base_name]
        modules = modules + [
            PACKAGE_NAME.replace('/', '.') + '.%s_loader' % base_name
        ]
    content = '\n'.join(['import %s' % m for m in modules])
    native.genrule(
        name=name + '_loader',
        outs=[name + '_loader.py'],
        cmd='echo "%s" > $@' % content)
    native.py_library(
        name=name,
        deps=lib_deps,
        srcs=[':' + name + '_loader'],
        visibility=visibility)
