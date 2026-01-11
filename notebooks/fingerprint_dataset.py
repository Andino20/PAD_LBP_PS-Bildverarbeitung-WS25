import os
import re
import pandas as pd
from PIL import Image
from sklearn.model_selection import GroupKFold

class FingerprintDataset:
    def __init__(self, directory, pattern, rename_map=None):
        """
        Args:
            directory (str): Path to the folder containing images.
            pattern (str): Regex with named groups
            rename_map (dict): Dictionary to rename columns.
        """
        self.directory = directory
        self.pattern = re.compile(pattern)
        self.rename_map = rename_map or {}
        self.data = self._load_metadata()

    def _load_metadata(self):
        records = []
        # os.walk yields (current_path, subdirectories, files)
        for root, _, files in os.walk(self.directory):
            for filename in files:
                match = self.pattern.search(filename)
                if match:
                    info = match.groupdict()
                    info['file_path'] = os.path.join(root, filename)
                    records.append(info)
        
        df = pd.DataFrame(records)
        
        if self.rename_map and not df.empty:
            df = df.rename(columns=self.rename_map)
            
        return df

    def filter_by_df(self, other_df, on_columns):
        """
        Keeps only the rows where the values in 'on_columns' 
        exist in 'other_df'.
        
        Args:
            other_df (pd.DataFrame): The reference dataframe.
            on_columns (list): List of column names to match (e.g., ['id', 'finger']).
        """
        # Drop duplicates to ensure we don't multiply rows in our main dataset
        other_df = other_df[on_columns].drop_duplicates()
        # We perform an inner merge on only the columns we care about.
        # This effectively filters 'self.data' to only include matches.
        self.data = self.data.merge(other_df, on=on_columns, how='inner')
        # Reset index to ensure consistency after rows are dropped
        self.data = self.data.reset_index(drop=True)
        return self
    
    def get_df(self):
        """Returns a copy of the internal metadata dataframe."""
        return self.data.copy()

    def get_df_mut(self):
        """Returns a mutable reference to the internal metadata dataframe."""
        return self.data
    
    def __len__(self):
        return len(self.data)
