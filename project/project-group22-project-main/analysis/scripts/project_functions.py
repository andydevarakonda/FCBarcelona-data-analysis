import pandas as pd

def load_process(path_to_csv):
    file = pd.read_csv(path_to_csv)
    df= pd.DataFrame(file)
    updt_df = (file.iloc[0:len(df), 1:22])

    barcelona_home= (updt_df[updt_df['HomeTeam']== 'Barcelona'])
    barcelona_away= (updt_df[updt_df['AwayTeam']== 'Barcelona'])
    barcelona = (pd.concat([barcelona_home,barcelona_away]))


    realmadrid_home= updt_df[updt_df['HomeTeam']== 'Real Madrid']
    realmadrid_away= updt_df[updt_df['AwayTeam']== 'Real Madrid']
    realmadrid = pd.concat([realmadrid_home,realmadrid_away])


    atletico_home= updt_df[updt_df['HomeTeam']== 'Ath Madrid']
    atletico_away= updt_df[updt_df['AwayTeam']== 'Ath Madrid']
    atletico_madrid = pd.concat([atletico_home,atletico_away])


    valencia_home= updt_df[updt_df['HomeTeam']== 'Valencia']
    valencia_away= updt_df[updt_df['AwayTeam']== 'Valencia']
    valencia = pd.concat([valencia_home,valencia_away])

    top_4 = (pd.concat([barcelona, realmadrid, atletico_madrid, valencia]))
    return top_4

def getBarcelona():
    barcelona_home= (updt_df[updt_df['HomeTeam']== 'Barcelona'])
    barcelona_away= (updt_df[updt_df['AwayTeam']== 'Barcelona'])
    barcelona = (pd.concat([barcelona_home,barcelona_away]))
    return barcelona
