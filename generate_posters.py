import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 确保输出目录存在
output_dir = 'd:/jinyuliangyuan/assets/posters'
os.makedirs(output_dir, exist_ok=True)

# 字体配置
FONT_YAHEI_BOLD = 'C:/Windows/Fonts/msyhbd.ttc'
FONT_YAHEI = 'C:/Windows/Fonts/msyh.ttc'
FONT_SONG_BOLD = 'C:/Windows/Fonts/simsunb.ttf'
FONT_SONG = 'C:/Windows/Fonts/simsun.ttc'
FONT_KAI = 'C:/Windows/Fonts/simkai.ttf'

def get_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.truetype(FONT_YAHEI, size)

# 自动多行文本绘制辅助函数
def draw_text_wrapped(draw, xy, text, font, fill, max_width, line_spacing=1.4):
    x, y = xy
    lines = []
    current_line = ""
    for char in text:
        test_line = current_line + char
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)

    cur_y = y
    line_h = int(font.size * line_spacing)
    for line in lines:
        draw.text((x, cur_y), line, font=font, fill=fill)
        cur_y += line_h
    return cur_y

# 逐字绘制以增加字间距
def draw_text_spaced(draw, xy, text, font, fill, spacing=10):
    x, y = xy
    cur_x = x
    for char in text:
        draw.text((cur_x, y), char, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), char, font=font)
        cur_x += (bbox[2] - bbox[0]) + spacing
    return cur_x

# 颜色常量
COLOR_GOLD = (212, 175, 55)
COLOR_GOLD_LIGHT = (245, 225, 140)
COLOR_RED = (196, 30, 58)
COLOR_RED_DARK = (139, 0, 0)
COLOR_INK = (17, 12, 7)
COLOR_CREAM = (250, 246, 238)
COLOR_CREAM_SOFT = (244, 237, 224)
COLOR_WHITE = (255, 255, 255)
COLOR_TEXT_DARK = (31, 23, 18)
COLOR_TEXT_MUTED = (95, 78, 65)

WIDTH = 1080

# ══════════════════════════════════════════════════════
# 海报 1：源头工厂首屏海报 (Header & Hook)
# ══════════════════════════════════════════════════════
def generate_poster_1():
    height = 1440
    im = Image.new('RGB', (WIDTH, height), COLOR_INK)
    draw = ImageDraw.Draw(im)

    # 1. 背景大图
    bg_craft = 'd:/jinyuliangyuan/assets/craft_process.jpg'
    if os.path.exists(bg_craft):
        bg_im = Image.open(bg_craft).convert('RGB')
        bg_im = bg_im.resize((WIDTH, int(WIDTH * bg_im.height / bg_im.width)))
        if bg_im.height < 740:
            bg_im = bg_im.resize((int(740 * bg_im.width / bg_im.height), 740))
        bg_crop = bg_im.crop((0, 0, WIDTH, 720))
        im.paste(bg_crop, (0, 0))

    # 渐变过渡遮罩
    overlay = Image.new('RGBA', (WIDTH, 720), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    for y in range(720):
        alpha = int((y / 720.0) ** 1.6 * 245) + 10
        ov_draw.line([(0, y), (WIDTH, y)], fill=(17, 12, 7, alpha))
    im.paste(overlay, (0, 0), overlay)

    # 下半部分温润米白底色
    draw.rectangle([(0, 710), (WIDTH, height)], fill=COLOR_CREAM)
    draw.line([(0, 710), (WIDTH, 710)], fill=COLOR_GOLD, width=3)

    # 顶部 Logo
    f_logo = get_font(FONT_YAHEI_BOLD, 36)
    f_tag = get_font(FONT_YAHEI, 26)
    logo_path = 'd:/jinyuliangyuan/logo.png'
    if os.path.exists(logo_path):
        logo_im = Image.open(logo_path).convert('RGBA').resize((68, 68))
        im.paste(logo_im, (60, 48), logo_im)
    draw.text((145, 48), "今遇莨缘 · 香云纱", font=f_logo, fill=COLOR_WHITE)
    draw.text((145, 94), "深圳非遗手工莨衣源头工厂", font=f_tag, fill=COLOR_GOLD_LIGHT)

    # 顶部 B 端直批红色胶囊徽标
    badge_x, badge_y = 60, 430
    draw.rectangle([(badge_x, badge_y), (badge_x + 360, badge_y + 48)], fill=COLOR_RED)
    f_badge = get_font(FONT_YAHEI_BOLD, 24)
    draw.text((badge_x + 25, badge_y + 10), "◆ B端专供 · 源头工厂直批", font=f_badge, fill=COLOR_WHITE)

    # 首屏大标题
    f_h1 = get_font(FONT_YAHEI_BOLD, 62)
    draw_text_spaced(draw, (60, 498), "深圳非遗手工莨衣", f_h1, COLOR_GOLD_LIGHT, spacing=6)
    
    f_h1_sub = get_font(FONT_YAHEI, 30)
    draw.text((60, 582), "专注高端手工香云纱批发 · 门店定向研发 · 贴牌定制", font=f_h1_sub, fill=COLOR_WHITE)

    # 核心引言金句 (米底部分，左侧金线)
    card_top = 760
    draw.rectangle([(60, card_top), (70, card_top + 340)], fill=COLOR_GOLD)
    
    f_quote_main = get_font(FONT_YAHEI_BOLD, 38)
    f_quote_sub = get_font(FONT_YAHEI, 30)
    draw.text((95, card_top + 10), "今遇莨缘香云纱，", font=f_quote_main, fill=COLOR_INK)
    draw.text((95, card_top + 75), "是深圳高品质纯手工香云纱源头设计工厂。", font=f_quote_main, fill=COLOR_RED)
    draw.text((95, card_top + 150), "家族深耕香云纱供应链十多年，", font=f_quote_sub, fill=COLOR_TEXT_DARK)
    draw.text((95, card_top + 210), "为全国国风实体店提供一手货源与灵活小单定制。", font=f_quote_sub, fill=COLOR_TEXT_DARK)
    draw.text((95, card_top + 280), "坚持五千年国风原创纹样 · 10-15天重工匠人交付", font=f_quote_sub, fill=COLOR_TEXT_MUTED)

    # 严正警示卡片
    warn_y = 1160
    draw.rectangle([(60, warn_y), (WIDTH - 60, warn_y + 120)], fill=(255, 240, 242), outline=COLOR_RED, width=2)
    f_warn_title = get_font(FONT_YAHEI_BOLD, 28)
    f_warn_desc = get_font(FONT_YAHEI, 24)
    draw.text((85, warn_y + 22), "【B端采购特别须知】", font=f_warn_title, fill=COLOR_RED)
    draw.text((85, warn_y + 65), "本通道专供全国实体店、二批、原创品牌合作，谢绝散客零售", font=f_warn_desc, fill=COLOR_INK)

    # 底部装饰线
    draw.line([(60, 1400), (WIDTH - 60, 1400)], fill=(220, 205, 185), width=2)

    out_file = os.path.join(output_dir, 'poster_01.jpg')
    im.save(out_file, quality=95)
    print('Generated poster_01.jpg')

# ══════════════════════════════════════════════════════
# 海报 2：一体两翼体系与六大硬核数据 (System & Metrics)
# ══════════════════════════════════════════════════════
def generate_poster_2():
    height = 1600
    im = Image.new('RGB', (WIDTH, height), COLOR_CREAM)
    draw = ImageDraw.Draw(im)

    # 顶部模块标签
    f_tag = get_font(FONT_YAHEI_BOLD, 22)
    draw.rectangle([(WIDTH//2 - 160, 60), (WIDTH//2 + 160, 100)], fill=COLOR_INK)
    draw.text((WIDTH//2 - 130, 68), "FACTORY CORE SYSTEM", font=f_tag, fill=COLOR_GOLD_LIGHT)

    # 模块标题
    f_sec_title = get_font(FONT_YAHEI_BOLD, 50)
    f_sec_sub = get_font(FONT_YAHEI, 26)
    draw.text((WIDTH//2 - 270, 125), "“一体两翼”源头工厂体系", font=f_sec_title, fill=COLOR_INK)
    draw.text((WIDTH//2 - 310, 195), "今遇莨缘如何为全国国风实体店筑造品质与利润护城河？", font=f_sec_sub, fill=COLOR_TEXT_MUTED)

    # 一体两翼体系大卡片
    card_x, card_y, card_w, card_h = 60, 250, WIDTH - 120, 520
    draw.rectangle([(card_x, card_y), (card_x + card_w, card_y + card_h)], fill=(245, 238, 225), outline=COLOR_GOLD, width=2)

    col_w = 450
    col_h = 320

    # 左侧：古法“不变”
    left_x, col_y = card_x + 25, card_y + 25
    draw.rectangle([(left_x, col_y), (left_x + col_w, col_y + col_h)], fill=COLOR_WHITE, outline=(220, 200, 170), width=1)
    f_col_t = get_font(FONT_YAHEI_BOLD, 32)
    draw.text((left_x + 130, col_y + 20), "古法“不变”", font=f_col_t, fill=COLOR_INK)
    draw.line([(left_x + 30, col_y + 65), (left_x + col_w - 30, col_y + 65)], fill=COLOR_GOLD, width=2)
    f_item = get_font(FONT_YAHEI, 24)
    items_left = [
        "◆ 顺德天然生态晒莨场",
        "◆ 薯莨浸染与富铁河泥日晒",
        "◆ 100%纯正非遗天然面料",
        "◆ 资深老匠人手工裁剪缝制"
    ]
    for i, it in enumerate(items_left):
        draw.text((left_x + 40, col_y + 90 + i * 52), it, font=f_item, fill=COLOR_TEXT_DARK)

    # 右侧：顺应时代“变”
    right_x = card_x + card_w - col_w - 25
    draw.rectangle([(right_x, col_y), (right_x + col_w, col_y + col_h)], fill=COLOR_WHITE, outline=(220, 200, 170), width=1)
    draw.text((right_x + 110, col_y + 20), "顺应时代“变”", font=f_col_t, fill=COLOR_RED)
    draw.line([(right_x + 30, col_y + 65), (right_x + col_w - 30, col_y + 65)], fill=COLOR_RED, width=2)
    items_right = [
        "◆ 溯源5000年国风原创纹样",
        "◆ 五行时令配色重工刺绣",
        "◆ 国人专属显瘦改良版型",
        "◆ 10-15天灵活小单快反"
    ]
    for i, it in enumerate(items_right):
        draw.text((right_x + 40, col_y + 90 + i * 52), it, font=f_item, fill=COLOR_TEXT_DARK)

    # 体系中央底座
    core_y = card_y + col_h + 45
    draw.rectangle([(card_x + 25, core_y), (card_x + card_w - 25, core_y + 110)], fill=COLOR_INK, outline=COLOR_GOLD, width=2)
    f_core_t = get_font(FONT_YAHEI_BOLD, 30)
    f_core_s = get_font(FONT_YAHEI, 22)
    draw.text((card_x + 310, core_y + 18), "今遇莨缘 · 核心供应链体系", font=f_core_t, fill=COLOR_GOLD_LIGHT)
    draw.text((card_x + 290, core_y + 62), "全流程匠人精工品控 ｜ 自有四大独立生产车间", font=f_core_s, fill=(230, 220, 200))

    # ════ 六大硬核数据 ════
    sec2_y = 830
    draw.rectangle([(WIDTH//2 - 150, sec2_y), (WIDTH//2 + 150, sec2_y + 40)], fill=COLOR_INK)
    draw.text((WIDTH//2 - 120, sec2_y + 8), "HARDCORE METRICS", font=f_tag, fill=COLOR_GOLD_LIGHT)

    draw.text((WIDTH//2 - 180, sec2_y + 60), "六大硬核实力数据", font=f_sec_title, fill=COLOR_INK)

    # 2x3 数据网格
    grid_y = sec2_y + 140
    metrics = [
        ("10+年", "家族深耕供应链", "专注于高品质手工香云纱研发"),
        ("4大", "独立硬性车间", "晒莨场/设计部/缝制车间/制版间"),
        ("10-15天", "重工交付周期", "单件重工制作，小单快速翻单"),
        ("100%", "正宗非遗薯莨染", "古法多重固色，久穿不褪色泛白"),
        ("200+家", "合作实体门店", "覆盖全国一二线国风高端买手店"),
        ("0加价", "一手工厂直批", "无中间商赚差价，实体店利润足"),
    ]

    box_w = 460
    box_h = 160
    for i, (num, title, desc) in enumerate(metrics):
        row = i // 2
        col = i % 2
        bx = 60 + col * (box_w + 40)
        by = grid_y + row * (box_h + 20)

        draw.rectangle([(bx, by), (bx + box_w, by + box_h)], fill=COLOR_WHITE, outline=(225, 210, 185), width=2)
        
        f_num = get_font(FONT_YAHEI_BOLD, 46)
        f_mtit = get_font(FONT_YAHEI_BOLD, 26)
        f_mdesc = get_font(FONT_YAHEI, 20)

        draw.text((bx + 25, by + 20), num, font=f_num, fill=COLOR_RED)
        draw.text((bx + 25, by + 80), title, font=f_mtit, fill=COLOR_INK)
        draw.text((bx + 25, by + 118), desc, font=f_mdesc, fill=COLOR_TEXT_MUTED)

    out_file = os.path.join(output_dir, 'poster_02.jpg')
    im.save(out_file, quality=95)
    print('Generated poster_02.jpg')

# ══════════════════════════════════════════════════════
# 海报 3：四大合作模式 (Cooperation Modes)
# ══════════════════════════════════════════════════════
def generate_poster_3():
    height = 1560
    im = Image.new('RGB', (WIDTH, height), COLOR_CREAM)
    draw = ImageDraw.Draw(im)

    # 顶部标签
    f_tag = get_font(FONT_YAHEI_BOLD, 22)
    draw.rectangle([(WIDTH//2 - 160, 60), (WIDTH//2 + 160, 100)], fill=COLOR_INK)
    draw.text((WIDTH//2 - 130, 68), "COOPERATION MODES", font=f_tag, fill=COLOR_GOLD_LIGHT)

    f_sec_title = get_font(FONT_YAHEI_BOLD, 50)
    f_sec_sub = get_font(FONT_YAHEI, 26)
    draw.text((WIDTH//2 - 250, 125), "四大灵活 B 端合作模式", font=f_sec_title, fill=COLOR_INK)
    draw.text((WIDTH//2 - 310, 195), "量身定制的供应链解决方案，助您抢占国风高端市场", font=f_sec_sub, fill=COLOR_TEXT_MUTED)

    modes = [
        ("01", "高端香云纱现货批发", "当季热销爆款、经典斜襟套装、改良旗袍等全系列现货，一手工厂底价直发，快速抢占实体门店销售旺季。", ["现货库存直发", "支持混批选款", "实体店利润足"]),
        ("02", "国风门店独家定向研发", "根据您的门店客群定位量身设计专属款式，提供独家款号保护，彻底摆脱通货撞款与恶性价格战。", ["区域独家保护", "原创国风纹样", "时令专属刺绣"]),
        ("03", "品牌贴牌 OEM / ODM", "为中高端品牌、原创连锁提供全套代工贴牌。包工包料，定制专属领标、吊牌与包装，严格大厂质检交付。", ["全套专属辅料", "纯正非遗面料", "严苛大厂品控"]),
        ("04", "小批量个性化改版", "门槛极度灵活，支持小单试销与个性化版型微调，10-15天快速出货，大幅降低实体店备货压款风险。", ["灵活小单起订", "10-15天交货", "快速翻单响应"])
    ]

    card_y = 250
    card_h = 290
    f_num = get_font(FONT_YAHEI_BOLD, 30)
    f_ctitle = get_font(FONT_YAHEI_BOLD, 32)
    f_cdesc = get_font(FONT_YAHEI, 24)
    f_pill = get_font(FONT_YAHEI_BOLD, 20)

    for i, (num, title, desc, pills) in enumerate(modes):
        cy = card_y + i * (card_h + 25)
        draw.rectangle([(60, cy), (WIDTH - 60, cy + card_h)], fill=COLOR_WHITE, outline=(225, 210, 185), width=2)

        # 序号徽章
        draw.rectangle([(90, cy + 25), (150, cy + 70)], fill=COLOR_RED)
        draw.text((102, cy + 30), num, font=f_num, fill=COLOR_WHITE)

        # 标题
        draw.text((170, cy + 28), title, font=f_ctitle, fill=COLOR_INK)

        # 描述 (自动换行，避免溢出)
        draw_text_wrapped(draw, (90, cy + 90), desc, f_cdesc, COLOR_TEXT_MUTED, max_width=WIDTH - 200, line_spacing=1.5)

        # 标签 Pills
        px = 90
        for pill in pills:
            pill_w = len(pill) * 22 + 40
            draw.rectangle([(px, cy + 215), (px + pill_w, cy + 260)], fill=(245, 240, 230), outline=COLOR_GOLD, width=1)
            draw.text((px + 15, cy + 225), f"◆ {pill}", font=f_pill, fill=COLOR_TEXT_DARK)
            px += pill_w + 15

    out_file = os.path.join(output_dir, 'poster_03.jpg')
    im.save(out_file, quality=95)
    print('Generated poster_03.jpg')

# ══════════════════════════════════════════════════════
# 海报 4：批发展厅与官方微信直连 (Showroom & Contact)
# ══════════════════════════════════════════════════════
def generate_poster_4():
    height = 1520
    im = Image.new('RGB', (WIDTH, height), COLOR_INK)
    draw = ImageDraw.Draw(im)

    # 顶部标签
    f_tag = get_font(FONT_YAHEI_BOLD, 22)
    draw.rectangle([(WIDTH//2 - 160, 60), (WIDTH//2 + 160, 100)], fill=COLOR_RED)
    draw.text((WIDTH//2 - 130, 68), "OFFLINE SHOWROOM", font=f_tag, fill=COLOR_WHITE)

    f_sec_title = get_font(FONT_YAHEI_BOLD, 52)
    f_sec_sub = get_font(FONT_YAHEI, 26)
    draw.text((WIDTH//2 - 310, 130), "深圳南油 103 专属批发展厅", font=f_sec_title, fill=COLOR_GOLD_LIGHT)
    
    desc_lines = [
        "我们在深圳市南山区南油第一工业区 103 名品馆设有专属高阶批发展厅。",
        "全系列香云纱现货样衣沉浸式陈列，欢迎预约莅临品鉴、触摸面料手感与试穿样衣！"
    ]
    for i, dl in enumerate(desc_lines):
        draw.text((WIDTH//2 - 420, 210 + i * 40), dl, font=f_sec_sub, fill=(230, 220, 205))

    # 展厅地址卡片
    addr_y = 310
    draw.rectangle([(80, addr_y), (WIDTH - 80, addr_y + 240)], fill=(28, 20, 12), outline=COLOR_GOLD, width=2)

    f_addr = get_font(FONT_YAHEI, 28)
    f_addr_b = get_font(FONT_YAHEI_BOLD, 28)
    draw.text((120, addr_y + 30), "【展厅地址】", font=f_addr_b, fill=COLOR_GOLD_LIGHT)
    draw.text((290, addr_y + 30), "深圳市南山区南油第一工业区 103 名品馆", font=f_addr, fill=COLOR_WHITE)

    draw.text((120, addr_y + 95), "【采购专线】", font=f_addr_b, fill=COLOR_GOLD_LIGHT)
    draw.text((290, addr_y + 95), "198-9030-9398 · 莨哥（微信同号）", font=f_addr, fill=COLOR_GOLD_LIGHT)

    draw.text((120, addr_y + 165), "【采购特别说明】 仅接待 B 端实体店与品牌采购，谢绝散客零售", font=f_addr_b, fill=(255, 120, 120))

    # 微信二维码卡片
    qr_bg_y = 600
    qr_card_w = 560
    qr_card_h = 620
    qr_x = WIDTH//2 - qr_card_w//2
    draw.rectangle([(qr_x, qr_bg_y), (qr_x + qr_card_w, qr_bg_y + qr_card_h)], fill=COLOR_WHITE, outline=COLOR_GOLD, width=3)

    # 载入二维码
    qr_path = 'd:/jinyuliangyuan/assets/wechat_qr.png'
    if os.path.exists(qr_path):
        qr_im = Image.open(qr_path).convert('RGB').resize((420, 420))
        im.paste(qr_im, (WIDTH//2 - 210, qr_bg_y + 40))

    f_qr_t = get_font(FONT_YAHEI_BOLD, 32)
    f_qr_s = get_font(FONT_YAHEI, 24)
    draw.text((WIDTH//2 - 200, qr_bg_y + 490), "扫码或长按识别 · 添加官方微信", font=f_qr_t, fill=COLOR_INK)
    draw.text((WIDTH//2 - 160, qr_bg_y + 545), "微信号 / 手机同号：198-9030-9398", font=f_qr_s, fill=COLOR_RED)

    # 底部电话直拨醒目大按钮
    btn_y = 1280
    draw.rectangle([(120, btn_y), (WIDTH - 120, btn_y + 110)], fill=COLOR_RED)
    f_btn = get_font(FONT_YAHEI_BOLD, 36)
    draw.text((WIDTH//2 - 310, btn_y + 32), "◆ 一键拨打创始人热线 198-9030-9398", font=f_btn, fill=COLOR_WHITE)

    # 页脚版权
    f_foot = get_font(FONT_YAHEI, 20)
    draw.text((WIDTH//2 - 270, 1440), "© 2025 今遇莨缘香云纱 · 深圳非遗手工莨衣源头设计工厂", font=f_foot, fill=(150, 140, 130))

    out_file = os.path.join(output_dir, 'poster_04.jpg')
    im.save(out_file, quality=95)
    print('Generated poster_04.jpg')

generate_poster_1()
generate_poster_2()
generate_poster_3()
generate_poster_4()
print('All 4 polished posters generated successfully!')
