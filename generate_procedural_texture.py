# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

def generate_procedural_xiangyun_texture(width=2688, height=1848, seed=42):
    np.random.seed(seed)
    
    # 1. Base dark obsidian to rich bronze lacquer gradient
    y = np.linspace(0, 1, height)[:, None]
    x = np.linspace(0, 1, width)[None, :]
    
    # Diagonal luxury lighting angle
    light_map = 0.6 * np.exp(-((x - 0.75)**2 + (y - 0.35)**2) / 0.45) + 0.4 * (1 - y * 0.5)
    
    # Base dark bronze/obsidian colors
    # Color A (dark obsidian): [14, 10, 8]
    # Color B (rich warm bronze): [48, 30, 20]
    # Color C (golden amber highlight): [85, 56, 32]
    
    base_r = 14 + (48 - 14) * light_map + 25 * np.exp(-((x - 0.7)**2 + (y - 0.4)**2) / 0.15)
    base_g = 10 + (30 - 10) * light_map + 16 * np.exp(-((x - 0.7)**2 + (y - 0.4)**2) / 0.15)
    base_b = 8 + (20 - 8) * light_map + 8 * np.exp(-((x - 0.7)**2 + (y - 0.4)**2) / 0.15)
    
    # 2. Fabric weave noise (micro horizontal & vertical threads)
    weave_h = np.sin(np.arange(height)[:, None] * 1.8) * 2.5
    weave_v = np.sin(np.arange(width)[None, :] * 1.8) * 2.5
    weave = weave_h + weave_v
    
    # 3. Organic Gambiered Silk Craquelure (Voronoi-like micro crack lines)
    # Generate random points for Voronoi cells
    num_points = 350
    pts_x = np.random.uniform(0, width, num_points)
    pts_y = np.random.uniform(0, height, num_points)
    
    # Fast grid approximation for craquelure
    crack_map = np.zeros((height, width), dtype=np.float32)
    # Add subtle fractal noise
    noise = np.random.normal(0, 4.0, (height, width))
    
    r = np.clip(base_r + weave + noise * 0.5, 0, 255).astype(np.uint8)
    g = np.clip(base_g + weave + noise * 0.4, 0, 255).astype(np.uint8)
    b = np.clip(base_b + weave + noise * 0.3, 0, 255).astype(np.uint8)
    
    img_arr = np.stack([r, g, b], axis=-1)
    img = Image.fromarray(img_arr, mode='RGB')
    
    # Subtle blur to blend weave
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    
    # Draw organic delicate golden crackle lines on overlay
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw subtle craquelure lines
    for i in range(num_points):
        x1, y1 = pts_x[i], pts_y[i]
        # Connect to 2 nearest points
        dists = (pts_x - x1)**2 + (pts_y - y1)**2
        nearest = np.argsort(dists)[1:4]
        for n_idx in nearest:
            x2, y2 = pts_x[n_idx], pts_y[n_idx]
            if dists[n_idx] < 220**2:
                # Wobbly line
                mx, my = (x1 + x2)/2 + np.random.uniform(-15, 15), (y1 + y2)/2 + np.random.uniform(-15, 15)
                # Golden subtle crackle color
                alpha = int(np.random.uniform(15, 45))
                gold_val = (195, 155, 95, alpha)
                draw.line([(x1, y1), (mx, my), (x2, y2)], fill=gold_val, width=np.random.choice([1, 2]))
    
    # Gold leaf / dust specks
    for _ in range(600):
        gx = np.random.uniform(0, width)
        gy = np.random.uniform(0, height)
        grad_alpha = int(np.random.uniform(25, 90) * (0.3 + 0.7 * (gx / width)))
        draw.ellipse([gx, gy, gx + np.random.uniform(1, 3.5), gy + np.random.uniform(1, 3.5)], 
                     fill=(212, 175, 55, grad_alpha))
                     
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=0.8))
    img.paste(Image.alpha_composite(Image.new("RGBA", (width, height), (0,0,0,255)), overlay).convert("RGB"), (0,0), overlay)
    
    return img

if __name__ == "__main__":
    tex = generate_procedural_xiangyun_texture(2688, 1848)
    tex.save(r"d:\jinyuliangyuan\procedural_silk_texture_sample.jpg", quality=98)
    print("Texture generated successfully!")
