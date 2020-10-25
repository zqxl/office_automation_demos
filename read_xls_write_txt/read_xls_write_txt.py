import os
import xlrd

file_name = 'regs.xlsx'

print(os.getcwd())

excel_file = os.getcwd() + '\\' + file_name

book = xlrd.open_workbook(excel_file)
sh = []
for i in range(0, book.nsheets):
    sh.append(book.sheet_by_index(i))
    print("sheet index:%d, name:%s, ncols:%d, nrows:%d" % (i, sh[i].name, sh[i].ncols, sh[i].nrows))

rst = 'u32 reg[][2] = {\n'

for r_i in range(8, sh[0].nrows):
    rst = rst + '\t{' + str(sh[0].cell_value(r_i, 3)) + ', ' + str(sh[0].cell_value(r_i, 4)) + '},\n'
rst = rst + '};'
print(rst)

rst_txt = open('regs.c', 'w')
rst_txt.write(rst)
rst_txt.close()
