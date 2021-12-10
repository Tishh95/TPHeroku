
class DataHandler():

    def __init__(self):
            df = pd.read_csv('parEncoreChoisi.csv', delimiter=",")
            try:
                df2 = pd.read_csv('pasEncoreChoisi2.csv', delimiter=",")
            except:
                df = pd.merge(df , df2 , on ="sameColumn" , how='outer')
            return df


    class FeatureRecipe:
        “”"
        Feature processing class
        “”"
        def __init__(self, data: pd.DataFrame):
            self.data = data
            self.continuous = None
            self.categorical = None
            self.discrete = None
            self.datetime = None
