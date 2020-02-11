def word_spliter(df):
  result = []
  l1 = df['Tweets']
  for tweet in l1:
    result.append(tweet.lower().split(' '))
  df['Split words'] = result
  return df