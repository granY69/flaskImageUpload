from PIL import Image#, ImageEnhance

def enhance_image(file_path):
    img = Image.open(file_path)
    print(f"Pixels are {img.size}")
    new_size = (1080, 1080)
    
    new_img = img.resize(new_size)
    print(f"Pixels are {new_img.size}")
    
    # enhancer = ImageEnhance.Brightness(new_img)
    # new_img = enhancer.enhance(1.5)
    
    new_img = new_img.convert('L')
    return new_img#.save(r'new_'+file_path)
# enhance_image(r'Box Back.jpg')