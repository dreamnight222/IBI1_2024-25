#Step 1:Make the list
uk_countries=[57.11,3.13,1.91,5.45]
Zhejiangneighbouring_provinces=[65.77,41.88,45.28,61.27,85.15]
#Step 2:Sort and print
uk_sorted=sorted(uk_countries)
Zhejiang_sorted=sorted(Zhejiangneighbouring_provinces)
print("populations of countries in the UK:", uk_sorted)
print("populations of Zhejiang-neighbouring provinces in China:", Zhejiang_sorted)
#Step 3:Draw the pie charts
#Pseudocode：
#1.Create a figure that big enough
#2.Define labels for UK and Zhejiang
#3.Creat pie charts for UK
#4.Creat pie charts for Zhejiang
#5.show the charts properly
#1.
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))#width 12 inch, height 6 inch
#2.
uk_labels = ["England","Wales","Northern Ireland","Scotland"]
Zhejiang_labels = ["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
#3.
plt.subplot(1,2,1)
plt.pie(uk_countries, labels=uk_labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title("UK countries population distribution")
plt.axis('equal')
#4.
plt.subplot(1,2,2)
plt.pie(Zhejiangneighbouring_provinces, labels=Zhejiang_labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title("Zhejiang neighbouring provinces population distribution")
plt.axis('equal')
#5.
plt.tight_layout(pad=2.0)
plt.show()