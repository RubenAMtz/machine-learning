# Definition:
# IG for feature A that splits a set of examples S into {S1, . . . ,Sm} :
# IG(S,A) = (original entropy) - (entropy after split)
# IG(S,A) = H(S) Sum, from i=1 to m, |Si|/|S| * H(Si)

# Information Gain = IG
# Entropy = H
# Set = S
# Subset = Si
# Feature = A

# Selects a feature and tests if that feature creates the most information gain.
# Meaning that the greater the result (of IG) the better (thus, we gain more information, or things are less uncertain)
# H(S) = Entropy of the whole set
# H(Si) = Entropy of a subset

#10 features. We have to calculate IG 10 times, in order to select an appropiate feature to split.

# Nodes
# Tree
# Inside nodes are (Si)

# Example   Alternate Bar   Fri/Sat Hungry  Patrons Price   Raining Reservation Type        WaitEst  |   WillWait?
# ----------------------------------------------------------------------------------------------------------------
# 1         Yes       No    No      Yes     Some    €€€     No      Yes         French      0-10     |   Yes
# 2         Yes       No    No      Yes     Full    €       No      No          Thai        30-60    |   No
# 3         No        Yes   No      No      Some    €       No      No          Burger      0-10     |   Yes
# 4         Yes       No    Yes     Yes     Full    €       No      No          Thai        10-30    |   Yes
# 5         Yes       No    Yes     No      Full    €€€     No      Yes         French      >60      |   No
# 6         No        Yes   No      Yes     Some    €€      Yes     Yes         Italian     0-10     |   Yes
# 7         No        Yes   No      No      None    €       Yes     No          Burger      0-10     |   No
# 8         No        No    No      Yes     Some    €€      Yes     Yes         Thai        0-10     |   Yes
# 9         No        Yes   Yes     No      Full    €       Yes     No          Burger      >60      |   No
# 10        Yes       Yes   Yes     Yes     Full    €€€     No      Yes         Italian     10-30    |   No
# 11        No        No    No      No      None    €       No      No          Thai        0-10     |   No
# 12        Yes       Yes   Yes     Yes     Full    €       No      No          Burger      30-60    |   Yes

#IG(S,A) = H(S) Sum, from i=1 to m, |Si|/|S| * H(Si)
# H(S) = (-)Sum, from i=1 to m, pi*log2(pi)
# pi = relative frequency or probability of the class Ci

# ID3( S ):
# • IF all examples in S belong to the same class C THEN
    # – Return new leaf node and label it with class C.
# • ELSE
    # – Select a feature A based on some feature selection criterion.
    # – Generate a new tree node with A as the test feature.
    # – FOR EACH value vi of A:
        # Let Si ⇢ S contain all examples with A = vi.
        # Build subtree by applying ID3( Si )

import math

class DecisionTree:
    def __init__(self):
        self._foo = None
    
    def entropy(self, target):
        uniques = self.unique_elements(target)
        h = 0        
        for item in uniques:
            pi = self.relative_frequency(target, item)
            h = h - pi*math.log(pi, 2)
        return h

    #IG(S,A) = H(S) Sum, from i=1 to m, |Si|/|S| * H(Si)
    #def information_gain(self, target):
    def nodes_from_feature(self, feature):
        return len(self.unique_elements(feature))

    def classes_in_nodes(self, feature):
        return self.unique_elements(feature)

    

    # return un vector booleano correspondiente a la opcion
    def unique_logical(self, option, features):
        index = []
        for i in features:
            if i == option:
                index.append(True)
            else:
                index.append(False)
        return index

    def elements_in_node(self, features, target):
        unique_features = self.unique_elements(features)
        #elements = []
        # mira, aqui crea empty dictionary {} Yes!
        elements = {}
        for option in unique_features:
            logic_vector = self.unique_logical(option, features)                                           
            filtro = list(map(self.logical_filter, logic_vector, target))
            filtro = list(filter(lambda item: item != None, filtro))
            #aqui estas pusheando cada vector a elements vector
            # en lugar de eso, crea un nuevo "key" en el dictionary dictionary["keyname"] = somevalue
            elements[option] = filtro
            #elements.append({option: filtro})
        return elements

    @staticmethod
    def unique_elements(feature):
        return list(set(feature))

    @staticmethod
    def relative_frequency(target, item):
        return target.count(item) / len(target)

    @staticmethod    
    def logical_filter(boolean_value, target_value):
            if boolean_value == True:
                return boolean_value * target_value
            #return None

def test():
    t = DecisionTree()
    patrons = ["Some", "Full", "Some", "Full", "Full", "Some", "None", "Some", "Full", "Full", "None", "Full"]
    will_wait = ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No", "No", "Yes"]
    elements = t.elements_in_node(patrons,will_wait)
    print(elements)
    print(elements["None"])
    print(elements["Some"])
    print(elements["Full"])
    print(elements.keys())
    print(list(elements.keys()))
    keys = list(elements.keys())
    for option in elements.keys():
        print(option, t.entropy(elements[option]))
        entro = t.entropy(elements[option])
        print(elements[option])
        elements.update({option: 1})
    print(elements)
# run test function (outside class)
test()
