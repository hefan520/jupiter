import pandas as pd

def split_excel_file(input_file, rows_per_file):
    df = pd.read_excel(input_file)  # 读取 Excel 文件
    total_rows = len(df)
    file_count = (total_rows - 1) // rows_per_file + 1  # 计算需要拆分的文件数
    
    for i in range(file_count):
        start_row = i * rows_per_file
        end_row = start_row + rows_per_file
        if end_row > total_rows:
            end_row = total_rows
        
        # 创建拆分后的数据框
        split_df = df.iloc[start_row:end_row]
        
        # 保存拆分后的数据框到新的 Excel 文件
        output_file = f"output_{i+1}.xlsx"
        split_df.to_excel(output_file, index=False)

# 使用示例
input_file = "sn.xlsx"  # 输入的 Excel 文件名
rows_per_file = 5000  # 每个文件的行数

split_excel_file(input_file, rows_per_file)

