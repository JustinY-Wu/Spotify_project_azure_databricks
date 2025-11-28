class mold:
    
    def dropCol (self, df, col):
        df = df.drop(*col)
        return df
