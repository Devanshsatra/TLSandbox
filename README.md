# TLSandbox
Early Detection of Waves of Contagious Diseases

Initial Simple SIDHARTE V Model in 1 Dimension

Description of the Model
For our project, “Early trend prediction of contagious/infectious diseases”, we plan to use the Stochastic SIDHARTE V Model. The model is named after its six compartments: susceptible (S), infected (I), diagnosed (D), hospitalized (H), asymptomatic (A), recovered (R), treated (T), and deceased (E). The model is represented as a set of differential equations that describe the flow of individuals between these compartments over time.

1. dS/dt = -βS(I+αA) /N
2. dI/dt = βS(I+αA) /N - γI - δI
3. dD/dt = δI - κD
4. dH/dt = κD - φH - μH
5. dA/dt = -βS(I+αA) /N - ωA
6. dR/dt = γI + φH + μH + ωA
7. dT/dt = φH
8. dE/dt = μH

where S is the number of susceptible individuals, I is the number of infected individuals, D is the number of diagnosed individuals, H is the number of hospitalized individuals, A is the number of asymptomatic individuals, R is the number of recovered individuals, T is the number of treated individuals, E is the number of deceased individuals, and N is the total population size. The β parameter represents the transmission rate, which determines the rate at which the disease spreads from infected individuals to susceptible individuals. The α parameter represents the proportion of asymptomatic cases in the population, which can be infectious despite not showing any symptoms. The γ parameter represents the recovery rate, which determines the rate at which infected individuals recover and become immune to the disease. The δ parameter represents the rate at which individuals are diagnosed and moved into the diagnosed compartment. The κ parameter represents the rate at which diagnosed individuals are hospitalized. The φ parameter represents the rate at which hospitalized individuals recover or are treated, while the μ parameter represents the rate at which hospitalized individuals die from the disease. Finally, the ω parameter represents the rate at which asymptomatic individuals recover.

We shall be using the Gillespie algorithm. This algorithm is a stochastic simulation algorithm that can be used to simulate the stochastic behavior of chemical reaction systems. It can be adapted to model the spread of infectious diseases using the SIDHARTE V model, by treating the different compartments as chemical species and simulating the interactions between them.

Based on our problem statement of trend prediction for contagious diseases, a recurrent neural network (RNN) as we are working with time-series data, an RNN will be useful for capturing temporal dependencies and making predictions based on past trends.
