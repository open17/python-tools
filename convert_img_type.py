from PIL import Image
import os
import sys

def convert_img_type(source_path,target_type):
    try:
        # 打开原图片
        with Image.open(source_path) as im:
             # 转换为RGB模式
            rgb_im = im.convert("RGB")
            # 生成目标图片路径
            target_path = os.path.splitext(source_path)[0] + '.' + target_type.lower()
            # 保存目标图片
            rgb_im.save(target_path, target_type, quality=90)
        print(f"成功将图像转换为{target_type.upper()}图像！")
    except Exception as e:
        print(f"转换失败：{str(e)}")

if __name__ == "__main__":
    # 检查命令行参数数量
    if len(sys.argv) != 3:
        print("请提供正确的命令行参数！")
        print("用法: python convert_image.py <原图片路径> <目标图片类型>")
        sys.exit(1)
    # 获取命令行参数
    source_path = sys.argv[1]
    target_type =  sys.argv[2].upper()
    # 检查图片类型是否合法
    allowed_types = ["JPEG", "JPG", "PNG", "GIF", "BMP", "TIFF", "ICO"]
    if target_type not in allowed_types:
        print("不支持的图片类型！")
    else:
        # 检查原图片是否存在
        if not os.path.isfile(source_path):
            print("原图片不存在！")
        else:
            # 转换图片
           convert_img_type(source_path, target_type)