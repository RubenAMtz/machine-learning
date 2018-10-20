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
    
    def entropy(self, array):
        uniques = self.unique_elements(array)
        h = 0        
        for item in uniques:
            pi = self.relative_frequency(array, item)
            h = h - pi*math.log(pi, 2)
        return h

    def information_gain(self, parent, elements_in_node):
        """
        Calculates the Information Gain in node, using parent node entropy.
        
        Formula:
            IG = H(S) - Sum(|Si|/|S| * H(Si), from: i=1, to: m) 
        
        Where:
            H(S)    --  Entropy of parent (h_s)
            S       --  Set of elements
            Si      --  Subset of elements
            
        Keyword arguments:\n
            parent -- list of values from parent feature: (list)\n
            elements_in_node -- dictionary of elements in node: (dict)

        Return arguments:\n
            information gain -- float
        """
        s = self.total_elements_of(parent)
        h_s = self.entropy(parent)
        
        sum = 0
        for option in elements_in_node:
            h_si = self.entropy(elements_in_node[option])
            si = self.total_elements_of(elements_in_node[option])
            sum = sum + (si/s)*h_si
        return h_s - sum
    
    #def total_information_gain(self, target, elements_in_node):
    #    for i in features
    
    def nodes_from_feature(self, feature):
        """
        Returns the amount of unique elements of the argument feature.

        Keyword Arguments:\n
            feature -- a list with data of the feature: (list)
        
        Return Arguments:\n
            number -- amount of unique values in feature list: (number)                                                                                
        """        
        return len(self.unique_elements(feature))

    def classes_in_nodes(self, feature):
        """
        Wrapper for unique_elements which returns the unique elements of a list

        Keyword Arguments:\n
            array -- list of elements: (list)

        Return Arguments:\n
            list of unique elements: (list)            
        """        
        return self.unique_elements(feature)

    def total_elements_of(self, array):
        """
        Wrapper for getting the length of an array

        Keyword Arguments:\n
            array -- list of elements: (list)

        Return Arguments:\n
            length of array: (integer)
        """
        return len(array)

    def unique_logical(self, value, array):
        """
        Creates a logical vector using value to compare if it's in array list.
        If value is in array, it will generate True, in the same position of element in array.

        Keyword Arguments:\n
            value -- a value of any type
            array -- data of array (list)

        Return Arguments:\n
            logical_vector -- list containing boolean values
        """        
        logical_vector = []
        for item in array:
            if item == value:
                logical_vector.append(True)
            else:
                logical_vector.append(False)
        return logical_vector

    #elements in subgroups (nodes created due to tested feature)
    def elements_in_node(self, features, target):
        unique_features = self.unique_elements(features)
        elements = {}
        for option in unique_features:
            logic_vector = self.unique_logical(option, features)                                           
            filtro = list(map(self.logical_filter, logic_vector, target))
            filtro = list(filter(lambda item: item != None, filtro))
            elements[option] = filtro
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

def test():
    
    alternate = ["Yes","Yes","No","Yes","Yes","No","No","No","No","Yes","No","Yes"]
    bar = ["No","No","Yes","No","No","Yes","Yes","No","Yes","Yes","No","Yes"]
    fs = ["No","No","No","Yes","Yes","No","No","No","Yes","Yes","No","Yes"]
    hungry = ["Yes","Yes","No","Yes","No","Yes","No","Yes","No","Yes","No","Yes"]
    patrons = ["Some", "Full", "Some", "Full", "Full", "Some", "None", "Some", "Full", "Full", "None", "Full"]
    price = ["€€€","€","€""€","€€€","€€","€","€€","€","€€€","€","€"]
    raining = ["No","No","No","No","No","Yes","Yes","Yes","Yes","No","No","No"]
    reservation = ["Yes","No","No","No","Yes","Yes","No","Yes","No","Yes","No","No"]
    _type = ["French", "Thai", "Burger", "Thai", "French", "Italian", "Burger", "Thai", "Burger", "Italian", "Thai", "Burger"]
    will_wait = ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "No", "No", "Yes"]

    titles = ['alternate','bar','fs','hungry', 'patrons', 'price', 'raining', 'reservation', '_type']
    all_features = [alternate, bar, fs, hungry, patrons, price, raining, reservation, _type]
    
    features = {}
    for index, option in enumerate(titles):
        features[option] = all_features[index]
    print(features)

    
    t = DecisionTree()
    elements = t.elements_in_node(patrons,will_wait)
    print(elements)    
    print("Information Gain: ", t.information_gain(will_wait, elements))
    print(all_features[0])
# run test function (outside class)
test()
