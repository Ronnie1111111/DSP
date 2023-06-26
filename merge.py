def binary_to_hex(binary_string):
    if len(binary_string) != 64:
        return "错误: 输入的二进制字符串长度必须为64位"
    
    # 使用Python的内置函数将二进制字符串转换为十六进制字符串
    hex_string = hex(int(binary_string, 2))[2:]
    
    # 确保十六进制字符串长度为16位，不足时在左边填充0
    hex_string = hex_string.zfill(16)
    
    return hex_string


# 指定包含64位二进制字符串的文本文件的路径
input_file_path = 'datain.txt'

# 指定输出文件的路径
output_file_path = 'HEX_IIR.txt'

# 打开输出文件以写入转换结果
with open(output_file_path, 'w') as output_file:
    # 从输入文件中逐行读取二进制字符串
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            binary_data = line.strip()
            
            # 将64位二进制字符串转换为十六进制字符串
            converted_hex = binary_to_hex(binary_data)
            
            # 将十六进制字符串分成两个字符一组
            hex_pairs = ' '.join([converted_hex[i:i+2] for i in range(0, len(converted_hex), 2)])
            
            # 输出结果到控制台
            print(f"二进制数据: {binary_data}")
            print(f"转换后的十六进制数据(两个字符一组): {hex_pairs}")
            
            # 将转换结果写入到输出文件，并在每个结果后添加换行符
            output_file.write(hex_pairs + ' ')
