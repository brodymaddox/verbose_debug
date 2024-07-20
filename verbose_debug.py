'''
    Written by Brody Madddox
    Set of functions used to easily implement a debug system with a simple level parameter (verbose = {-1,0,1,2,3,4,5,6,7})

    Level Definition Key:
        
        Verbose = -1: No Warning Debug Prints
        Verbose = 0: No Debug Prints Display
        Verbose = 1: High-level code inter function debugs
        Verbose = 2: High-level Code intra function debugs
        Verbose = 3: Mid-level code inter function debugs
        Verbose = 4: Mid-level code intra function debugs
        Verbose = 5: Low-level code inter function debugs
        Verbose = 6: Low-level code intra function debugs
        Verbose = 7: The Kitchen Sink


        Warnings are implemented when a bug has been chased down and identified, to indicate if the same erroneous behavior is occurring
        High level code is somewhat defined as made up mostly of my own methods and being fairly abstract
        Mid level code is all other less abstract functions that do real implementation, but skips functions that do one fairly simple objective
        Low level code includes all of these very simple functions'
        The Kitchen Sink includes everything and extremely small debugs, perhaps in the middle of a complex algorithm

        Inter function debugs are debugs which indicate the input and output to a function
        Intra function debugs are debugs which are more or less randomly interspaced throughout a function, to check for proper dataflow
            (the most granular of these belong to The Kitchen Sink)
            
'''


def debug(text, args, verbosity, threshold):
    '''
        Function to display debug
        in:
            text : str text to display before args
            args : list of objects we intend to print in the debug
            verbosity : current verbosity within object being debugged
            threshold : the verbosity that triggers this delay
    '''
    
    # check if we should trigger
    if verbosity < threshold:
        return

    # figure out how much we should tab in by generating prefix
    prefix = '\t' * (threshold//2)  

    # display label and arguments using list comprehension
    print(f"{prefix} {text} {[str(arg) for arg in args]}")


def warning(text, verbosity):
    '''
        Function to display warning
        in:
            text : str text to display (excluding "WARNING: ")
            verbosity : current verbosity within the object being debugged
    '''

    # check if we should trigger, but we are a warning
    if verbosity <= -1:
        return
    
    # display label
    print(f"WARNING: {text}")
    
# If errors, run this file to run unit tests for the system with debug=True
debugging=True

if debugging:
    verbose = 8

    debug('test one', [i for i in range(10)], verbose, 1)
    debug('test two', [i for i in range(5)], verbose, 2)
    debug('test three', [i for i in range(10)], verbose, 3)
    debug('test four', [i for i in range(5)], verbose, 4)
    debug('test five', [i for i in range(10)], verbose, 5)
    debug('test six', [i for i in range(5)], verbose, 6)
    debug('test seven', [i for i in range(5)], verbose, 7)
    warning('warning', verbose)
