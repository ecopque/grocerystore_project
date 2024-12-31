# File: /draft.py

                if ask_categories == 1:
                    category = input('Enter the category you want to register: \n')
                    categorycontroller.register(category)

                elif ask_categories == 2:
                    category = input('Enter the category you want to remove: \n')
                    categorycontroller.remove(category)

                elif ask_categories == 3:
                    categoryold = input('Enter the category you want to change: \n')
                    categorynew = input('Enter the new category: \n')