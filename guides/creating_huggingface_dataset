# Routines for creating a Huggingface Dataset

The example here is from the Bokmål Nynorsk Balanced corpus. It is preshuffled and has a total of 9725051 lines. We are splitting this in a 90% train and a 5% validation and 5% test set.

Basically this means we are aiming for:
Train = 8752545
Validation = 486253
Test = 486253

'''
head -n 8752545 nb_nn_balanced_shuffled.json > nb_nn_balanced_shuffled_train.json
tail -n +8752546 nb_nn_balanced_shuffled.json > validation_and_test.json
head -n 486253 validation_and_test.json > nb_nn_balanced_shuffled_validation.json
tail -n +486254 validation_and_test.json > nb_nn_balanced_shuffled_validation.json
'''
