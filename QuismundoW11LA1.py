MachineLearning = [('Supervised', 'Decision Tree'), 
                   ('Supervised', 'Random Forest'), ('Unsupervised', 'K-Means'), 
                   ('Unsupervised', 'Gaussian Mixture Mode')]
 
for ML in ['Supervised', 'Unsupervised']:
    print("\nLearning Type: ", ML)
 
    for i in MachineLearning:
        if i[0]==ML:
            print(i[1])
