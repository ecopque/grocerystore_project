# File: /view.py

import controller

if __name__ == '__main__':
    while True:
        local = int(input('Enter 1 to access [Categories]\n'
                          'Enter 2 to access [Stock]\n'
                          'Enter 3 to access [Supplier]\n'
                          'Enter 4 to access [Customer]\n'
                          'Enter 5 to access [Employee]\n'
                          'Enter 6 to access [Sales]\n'
                          'Enter 7 to access see top selling products\n'
                          'Enter 8 to exit\n'))
        
        if local == 1:
            categorycontroller = controller.CategoryController()
            while True:
                decide = int(input('Enter 1 to register a category\n'
                                   'Enter 2 to remove a category\n'
                                   'Enter 3 to change a category\n'
                                   'Enter 4 to show registered categories\n'
                                   'Enter 5 to exit\n'))
                
                if decide == 1:
                    