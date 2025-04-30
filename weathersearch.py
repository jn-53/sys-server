import json
import time

import Levenshtein

# === 配置 ===
JSON_FILE = 'weather_district_id.json'  # 你的行政区json文件名


# === 步骤1：加载JSON数据 ===
def load_locations(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    locations = []
    for key, value in data.items():
        # 补充fullname字段（没有就生成）
        if 'fullname' not in value:
            fullname = key.replace('-', '')
            value['fullname'] = fullname
        locations.append(value)
    return locations


# === 步骤2：根据输入地名，找最相近的行政区 ===
def best_match(input_name, locations):
    best_score = float('inf')
    best_location = None
    for loc in locations:
        fullname = loc.get("fullname", "")
        score = Levenshtein.distance(input_name, fullname)
        if score < best_score:
            best_score = score
            best_location = loc
    return best_location, best_score


# === 主程序 ===
def main():
    locations = load_locations(JSON_FILE)
    print("=== 智能天气行政区查询 ===")

    while True:
        user_input = input("请输入想查询的地名（输入q退出）：").strip()
        if user_input.lower() == 'q':
            break
        if not user_input:
            continue

        start_time = time.time()  # 开始计时
        match, score = best_match(user_input, locations)
        end_time = time.time()  # 结束计时

        elapsed_ms = (end_time - start_time) * 1000  # 转成毫秒

        if match:
            print(f"最接近的行政区：{match['fullname']}（district_id: {match['district_id']}）")
            print(f"对应经纬度：({match['n']}, {match['e']})")
            print(f"匹配得分（越小越好）：{score}")
            print(f"匹配耗时：{elapsed_ms:.2f}ms")  # 打印耗时
        else:
            print("未找到匹配项。")


if __name__ == '__main__':
    main()
