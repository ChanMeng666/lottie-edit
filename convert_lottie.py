from PIL import Image
import base64
import io
import json

def invert_image_colors(base64_string):
    # 解码base64为图片
    img_data = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(img_data))
    
    # 如果有alpha通道,需要分离
    if img.mode == 'RGBA':
        r, g, b, a = img.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        
        # 反转RGB颜色
        inverted_rgb = Image.eval(rgb_image, lambda x: 255 - x)
        
        # 重新合并alpha通道
        r2, g2, b2 = inverted_rgb.split()
        inverted_image = Image.merge('RGBA', (r2, g2, b2, a))
    else:
        # 直接反转颜色
        inverted_image = Image.eval(img, lambda x: 255 - x)
    
    # 转回base64
    buffer = io.BytesIO()
    inverted_image.save(buffer, format='PNG')
    return base64.b64encode(buffer.getvalue()).decode()

# 读取原始JSON文件
with open('Animation-ClickMe.json', 'r') as f:
    data = json.load(f)

# 处理所有图片资源
for asset in data['assets']:
    if asset.get('p') and asset.get('p').startswith('data:image'):
        # 提取base64部分
        base64_data = asset['p'].split(',')[1]
        # 反转颜色
        inverted_base64 = invert_image_colors(base64_data)
        # 更新asset
        asset['p'] = f'data:image/png;base64,{inverted_base64}'

# 保存暗色主题JSON
with open('Animation-ClickMe-dark.json', 'w') as f:
    json.dump(data, f)