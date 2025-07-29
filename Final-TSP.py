import random
import math

# tarif tabe baraye mohasebe fasele bein do noghte
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# tarif class baraye masale foroshande doregard
class TravelingSalesmanGA:
    def __init__(self, cities, population_size=100, mutation_rate=0.01, generations=500):
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    # tolid jamiyat avalie
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = random.sample(self.cities, len(self.cities))
            population.append(individual)
        return population

    # tabe barazesh (mohasebe hazine safar)
    def fitness(self, individual):
        return sum(calculate_distance(individual[i], individual[i + 1]) for i in range(len(individual) - 1)) + \
               calculate_distance(individual[-1], individual[0])

    # entekhab valedein ba ravesh tournament
    def tournament_selection(self, population, k=5):
        tournament = random.sample(population, k)
        tournament.sort(key=self.fitness)
        return tournament[0]

    # tolid mesl (Crossover)
    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]

        pointer = 0
        for gene in parent2:
            if gene not in child:
                while child[pointer] is not None:
                    pointer += 1
                child[pointer] = gene
        return child

    # jahesh (Mutation)
    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(individual) - 1)
                individual[i], individual[j] = individual[j], individual[i]

    # takamol jamiyat
    def evolve(self, population):
        new_population = []
        for _ in range(self.population_size):
            parent1 = self.tournament_selection(population)
            parent2 = self.tournament_selection(population)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        return new_population

    # ejraye algorithm
    def run(self):
        population = self.initialize_population()
        for generation in range(self.generations):
            population = self.evolve(population)
            best_individual = min(population, key=self.fitness)
            best_cost = self.fitness(best_individual)
            print(f"Nasl {generation + 1}: kamtarin hazine = {best_cost:.2f}")
        return best_individual, self.fitness(best_individual)

# dadeh-haye masale: mokhtasat shahrha
cities = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 7), (8, 3), (7, 9), (2, 5)
]

# ejraye algorithm genetek
tsp = TravelingSalesmanGA(cities)
best_route, best_cost = tsp.run()

# namayesh behtarin masir va hazine
print("\nBehtarin masir peyda shode:")
for city in best_route:
    print(city, end=" -> ")
print(best_route[0])  # bargasht be shahr shoru
print(f"Hazine kol: {best_cost:.2f}")
