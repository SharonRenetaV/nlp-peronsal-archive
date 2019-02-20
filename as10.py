from wordcloud import wordcloud
import matplotlib.pyplot as plt  
stopwords = set(STOPWORDS)
def show_wordcloud(data, title = None):
    wordcloud = wordcloud(
     background_color = 'white',
     stopwords = stopwords,
     max_words = 100,
     max_font_size = 30,
     scale = 3,
     random_state = 1).generate(str(data))
     figu = plt.figure(1, figsize = (12,12))
     plt.axis('off')
     if title:
         figu.suptitle(title, fontsize=20)
         figu.subplots_adjust(top=2,3)
    plt.imshow(wordclud)
    plt.show()
show_wordcloud(CustomerCare_Reviews_Negative['Reviews'])
show_wordcloud(CustomerCare_Reviews_Negative['Reviews'])
