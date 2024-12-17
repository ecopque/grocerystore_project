# FILE: /report_code.md

- #1: Here, each element of 'cls.category' (which contains the category names) is passed as an argument to create a new object of 'CategoryModel' class. Each category read from the file will be used to instantiate a 'CategoryModel' object, which will be stored in the cat list.

- #2: I decided to replace it with 'for' loops as usual, eliminating as many built-in functions as possible.

- #3: Remember that 'items_sold' is of the 'ProductModel' class type, which has 'name', 'price' and 'category'.

- #4: Response: ['Fruits', 'Vegetables', 'Legumes'].

- #5: Response: ['bean|7|Legumes|Edson|Théo|3|14/12/2024'].

- #6: Response: [['bean', '7', 'Legumes', 'Edson', 'Théo', '3', '14/12/2024']].

- #7: Response: Théo.

- #8: Response: bean.

- #9: Response: 7.0.

- #10: Response: Category registered successfully.

- #11: Here, 'i' is an object of 'CategoryModel' class, which was created inside the read method of the 'CategoryDao' class. When the code gets to the line of 'if i.category == newcategory', it is accessing the category attribute of that 'CategoryModel' instance.