'''
Check that correct versions of each library are installed, and print warnings
or errors if not.
'''

#%% Housekeeping

__all__ = ['available', 'min_versions', 'check_sciris', 'check_synthpops']


available = {} # Make this available at the module level
min_versions = {'sciris':'0.17.2'}


#%% Check dependencies

def check_sciris():
    ''' Check that Sciris is available and the right version '''
    try:
        import sciris as sc
    except ModuleNotFoundError:
        errormsg = 'Sciris is a required dependency but is not found; please install via "pip install sciris"'
        raise ModuleNotFoundError(errormsg)
    ver = sc.__version__
    minver = min_versions['sciris']
    if sc.compareversions(ver, minver) < 0:
        errormsg = f'You have Sciris {ver} but {minver} is required; please upgrade via "pip install --upgrade sciris"'
        raise ImportError(errormsg)
    return


def check_synthpops(verbose=False, die=False):
    ''' Check whether synthpops is available '''

    # Check synthpops -- optional dependency
    try:
        import synthpops # noqa
        return synthpops
    except ImportError as E:
        import_error = f'Synthpops (for detailed demographic data) is not available ({str(E)})\n'
        if die:
            raise ImportError(import_error)
        elif verbose:
            print(import_error)
        return False

    return

# Perform the version checks on import
check_sciris()