import argparse
import json
from num_series import random_series, sine_series, trend_series, summarize

def main():
    parser = argparse.ArgumentParser(description="Генератор и статистика числовых рядов")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # random
    p_rand = subparsers.add_parser("random", help="Случайный ряд")
    p_rand.add_argument("-n", type=int, default=10, help="Количество точек")
    p_rand.add_argument("--low", type=float, default=-100.0, help="Нижняя граница")
    p_rand.add_argument("--high", type=float, default=100.0, help="Верхняя граница")
    p_rand.add_argument("--seed", type=int, default=None, help="Seed для воспроизводимости")

    # sine
    p_sine = subparsers.add_parser("sine", help="Синусоидальный ряд")
    p_sine.add_argument("-n", type=int, default=50, help="Количество точек")
    p_sine.add_argument("--amplitude", type=float, default=1.0, help="Амплитуда")
    p_sine.add_argument("--frequency", type=float, default=1.0, help="Частота")
    p_sine.add_argument("--noise", type=float, default=0.0, help="Уровень шума")
    p_sine.add_argument("--seed", type=int, default=None, help="Seed")

    # trend
    p_trend = subparsers.add_parser("trend", help="Линейный тренд")
    p_trend.add_argument("-n", type=int, default=20, help="Количество точек")
    p_trend.add_argument("--start", type=float, default=0.0, help="Начальное значение")
    p_trend.add_argument("--step", type=float, default=1.0, help="Шаг тренда")
    p_trend.add_argument("--noise", type=float, default=0.0, help="Шум")
    p_trend.add_argument("--seed", type=int, default=None, help="Seed")

    args = parser.parse_args()

    data = None
    if args.command == "random":
        data = random_series(args.n, low=args.low, high=args.high, seed=args.seed)
    elif args.command == "sine":
        data = sine_series(args.n, amplitude=args.amplitude, frequency=args.frequency,
                           noise=args.noise, seed=args.seed)
    elif args.command == "trend":
        data = trend_series(args.n, start=args.start, step=args.step,
                            noise=args.noise, seed=args.seed)

    if data is not None:
        summary = summarize(data)
        print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
