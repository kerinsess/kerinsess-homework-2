<
# Monte Carlo π — Parallel Computation

Обчислення числа π методом Монте-Карло з паралельними потоками.

## Параметри

| Параметр | Значення |
|---|---|
| N (точок) | 1M, 10M, 100M, 1B, 10B, 100B |
| M (потоків) | 1, 2, 4, 8, 16, 32, 64, 128 |

Усього комбінацій: **6 × 8 = 48**

## Запуск

```bash
pip install -r requirements.txt
python pi_monte_carlo_parallel.py
```

Результати зберігаються у `results/pi_monte_carlo_parallel_results.csv`.

## Формат CSV

```
N,M,pi_estimate,time_seconds
```

## Відомі обмеження

- Python GIL обмежує реальний паралелізм CPU-потоків — `ThreadPoolExecutor` дає виграш переважно при малих N.
- Запуск із великими N (≥ 10B) при M=1 займає значний час.
- Генератор псевдовипадкових чисел — стандартний `random.Random()`, не криптографічний.
=======
# #Karina_Medvedieva_KI-43-homework-2
tg: kerinsesss >>>>>>> main