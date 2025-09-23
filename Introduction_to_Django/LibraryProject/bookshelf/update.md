book1 = Book.objects.get(id='1')
book1.title = 'nineteen eighty four'
book1.save()
print(book1) 
"""<QuerySet [<nineteen eighty four>]>"""