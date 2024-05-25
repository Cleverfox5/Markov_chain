#include <iostream>
#include <cstdlib>
#include <ctime>
#include <map>
#include <vector>
#include <random>


using namespace std;

float randomValueFunction() {
    random_device rand;
    mt19937 gen(rand());
    uniform_real_distribution<> dis(0.0, 1.0);
    return dis(gen);
}

void step_by_step(int matrix[8][8], int steps, int start_condition_index) {
    int counter_visited[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    cout << "В результате " << steps << " шагов: \n\n";
    cout << "Траектория: ";
    for (int i = 0; i < steps; i++) {
        map<float, float> possibility;
        float memory = 0;
        for (int j = 0; j < 8; j++) {
            if (matrix[start_condition_index][j] != 0) {
                possibility[j] = matrix[start_condition_index][j] + memory;
                memory += matrix[start_condition_index][j];
            }
        }
        float rand_value = randomValueFunction();
        for (const auto& element : possibility) {
            if (element.second / 10 >= rand_value) {
                start_condition_index = element.first;
                counter_visited[start_condition_index]++;
                cout << start_condition_index + 1;
                break;
            }
        }
    }

    cout << "\nЧерез " << steps << " шагов - наступило событие:" << start_condition_index + 1 << "\n";
    cout << "Что касаемо остальных событий:\n";
    cout << "Посещено:\n";

    for (int i = 0; i < 8; i++)
        cout << i + 1 << " - " << counter_visited[i] << "\n";

    cout << "\nВ процентном соотношении:\n";

    for (int i = 0; i < 8; i++)
        cout << i + 1 << " - " << (float)counter_visited[i]/(float)steps << "\n";
    cout << "\n";
}

int main()
{
    setlocale(0, "");

    cout << "Цепь Маркова\n";

    int matrix[8][8] = {
        {4, 0, 2, 0, 4, 0, 0, 0},
        {0, 5, 0, 3, 0, 1, 0, 1},
        {2, 0, 4, 0, 4, 0, 0, 0},
        {0, 4, 0, 3, 0, 1, 0, 2},
        {4, 0, 5, 0, 1, 0, 0, 0},
        {0, 3, 0, 1, 0, 2, 0, 4},
        {0, 0, 1, 2, 4, 0, 1, 2},
        {0, 3, 0, 2, 0, 1, 0, 4} };


    cout << "\n\n\n";


    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++)
            cout << matrix[i][j] << " ";
        cout << "\n";
    }

    int start_condition_index;
    while (true) {
        cout << "Выберите событие с которого начнётся цепь (цифра 1-8)\n";
        cin >> start_condition_index;
        if (start_condition_index >= 1 && start_condition_index <= 8)
            break;
        cout << "Неправильный ввод - попробуйте снова\n";
    }

    start_condition_index--;

    step_by_step(matrix, 10, start_condition_index);
    step_by_step(matrix, 50, start_condition_index);
    step_by_step(matrix, 100, start_condition_index);
    step_by_step(matrix, 1000, start_condition_index);

    return 0;
}