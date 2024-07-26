from lib.common import *
from lib import log

__version__ = 1.0

BANNER = f"""{c.LIGHTCYAN_EX}
 **       **             **   **                 
/**      //             //   /**                 
/**       ** **********  ** ******  *****  ******
/**      /**//**//**//**/**///**/  **///**//**//*
/**      /** /** /** /**/**  /**  /******* /** / 
/**      /** /** /** /**/**  /**  /**////  /**   
/********/** *** /** /**/**  //** //******/***   
//////// // ///  //  // //    //   ////// ///{c.RESET}
V{__version__}
"""

if __name__ == '__main__':
    print(BANNER)
    from lib.request import *
    #url = input('URL -> ').strip() or None
    if url == None:
        print("Not input valid.")
    else:
        try:
            main()
        except KeyboardInterrupt:
            print("\r")
            print(log.error("Stopped!"), end="\r")