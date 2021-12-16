tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
  colWidths = [0] * len(tableData)
  
  for i in range(len(tableData)):
    for item in tableData[i]:
      if len(item) > colWidths[i]:
        colWidths[i] = len(item)
    
  
  for i in range(len(tableData[0])):
    for j in range(len(tableData)):
      print(tableData[j][i].rjust(colWidths[j]),end=' ')
    print()

printTable(tableData)
