import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import db_conn

parser = argparse.ArgumentParser()
parser.add_argument("--pagenumber",help="Enter the number of pages to parse", type=int)
parser.add_argument("--db_name",help="Enter the name of database", type=str)
args = parser.parse_args()

my_url = "https://www.meesho.com/men-clothing/pl/lb03x?page="
page_num_Max = args.pagenumber
scrapped_list = []
db_conn.connection(args.db_name)

for page_num in range(page_num_Max):
    req = requests.get(my_url + str(page_num))

    soup = BeautifulSoup(req.content,"html.parser")

    all_shirts = soup.find_all("div",{"class": "sc-dkPtyc ProductList__GridCol-sc-8lnc8o-0 dqIYJu ilkWHh"})

    for shirt in all_shirts:
        shirt_dict = {}
        shirt_dict["title"] = shirt.find("p",{"class": "Text__StyledText-oo0kvp-0 kEWsgb NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP"}).text
        shirt_dict["discount"] = shirt.find("span",{"class": "Text__StyledText-oo0kvp-0 dMKIzz NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja"}).text
        shirt_dict["price"] = shirt.find("h5",{"class": "Text__StyledText-oo0kvp-0 BBZyK"}).text
        shirt_dict["rating"] = shirt.find("span",{"class": "Text__StyledText-oo0kvp-0 UKsFl"}).text
        shirt_dict["Free_Delivery"] = shirt.find("span",{"class": "Text__StyledText-oo0kvp-0 fxlxQI"}).text

        #if shirt_delivery == "Free Delivery" :
            #shirt_dict["Free_Delivery"] = "Yes"
        scrapped_list.append(shirt_dict)
        db_conn.inserttable(args.db_name,tuple(shirt_dict.values()))

dataFrame = pandas.DataFrame(scrapped_list)
dataFrame.to_csv("meesho.csv")
    #print(shirt_name,shirt_price,shirt_discount,shirt_rating)
db_conn.get_info(args.db_name)













#<p color="greyT2" class="Text__StyledText-oo0kvp-0 kEWsgb NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP" font-size="16px" font-weight="book">Classic Fashionista Men Tshirts</p>
#<div class="sc-dkPtyc ProductList__GridCol-sc-8lnc8o-0 dqIYJu ilkWHh"><a href="/mens-stylish-casual-cotton-solid-tshirts-vol-4/p/k5so"><div color="white" class="Card__BaseCard-b3n78k-0 bABJTD NewProductCard__CardStyled-j0e7tu-0 lcNMDj NewProductCard__CardStyled-j0e7tu-0 lcNMDj"><div class="NewProductCard__ProductImage-j0e7tu-15 eHiFqj"><picture><source srcset="https://images.meesho.com/images/products/940632/1_400.webp" type="image/webp" class="lazyload"><img src="https://images.meesho.com/images/products/940632/1_400.jpg" width="100%" height="100%" class="lazyload NewProductCard__StyledPerfImage-j0e7tu-16 dKPFhT" alt="Mens Stylish Casual Cotton Solid T-Shirts Vol 4"></picture><div class="NewProductCard__Similar-j0e7tu-18 laobar"><span font-size="12px" font-weight="demi" color="greyT1" class="Text__StyledText-oo0kvp-0 jCIVHY">+5 More</span></div></div><div class="Card__BaseCard-b3n78k-0 kZcMvs NewProductCard__DetailCard_Desktop-j0e7tu-2 hnlpiX NewProductCard__DetailCard_Desktop-j0e7tu-2 hnlpiX" color="white"><p color="greyT2" class="Text__StyledText-oo0kvp-0 kEWsgb NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP NewProductCard__ProductTitle_Desktop-j0e7tu-4 kTeVKP" font-size="16px" font-weight="book">Mens Stylish Casual Cotton Solid T-Shirts Vol 4</p><div class="Card__BaseCard-b3n78k-0 BIuiq NewProductCard__PriceRow-j0e7tu-6 eaTfzM NewProductCard__PriceRow-j0e7tu-6 eaTfzM" color="white"><h5 color="greyBase" font-size="24px" font-weight="bold" class="Text__StyledText-oo0kvp-0 BBZyK">₹145</h5><p color="greyT2" font-size="16px" font-weight="book" class="Text__StyledText-oo0kvp-0 OJCfE Paragraph__StyledParagraphBody2StrikeThrough-sc-69qp0d-0 gKNxow Paragraph__StyledParagraphBody2StrikeThrough-sc-69qp0d-0 gKNxow">₹170</p><span color="greenBase" class="Text__StyledText-oo0kvp-0 dMKIzz NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja" font-size="16px" font-weight="demi">15% off</span></div><div class="Card__BaseCard-b3n78k-0 gegzNo NewProductCard__DiscountRow-j0e7tu-17 eYhoQI NewProductCard__DiscountRow-j0e7tu-17 eYhoQI" color="white"><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" height="16" width="16" color="greenT2" iconSize="20" class="Icon-sc-1iwi4w1-0 fXIWXj"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.833 5.733c0 .186 1.006 1.745 1.006 1.745.215.312-.844 2.27-.844 2.27-.105.151-.168 2.029-.168 2.029-.001.385-1.961 1.317-1.961 1.317-.17.058-1.276 1.54-1.276 1.54-.218.31-2.328-.139-2.328-.139-.17-.057-1.898.462-1.898.462-.352.118-1.806-1.541-1.806-1.541-.105-.151-1.796-.793-1.796-.793-.35-.12-.595-2.356-.595-2.356 0-.186-1.005-1.744-1.005-1.744-.215-.312.844-2.271.844-2.271.104-.151.167-2.029.167-2.029.002-.385 1.962-1.317 1.962-1.317.17-.058 1.275-1.54 1.275-1.54.218-.31 2.089.353 2.089.353.17.058 2.138-.676 2.138-.676l1.805 1.541c.106.151 1.797.793 1.797.793.35.12.594 2.356.594 2.356zM6.761 6.761a.875.875 0 11-1.238-1.237.875.875 0 011.238 1.237zm2.865-1.236a.6.6 0 11.848.849l-4.101 4.1a.6.6 0 11-.849-.848l4.102-4.1zm.846 4.95a.875.875 0 11-1.238-1.238.875.875 0 011.238 1.237z" fill="#06A759"></path></svg><span font-size="12px" font-weight="demi" color="greyT1" class="Text__StyledText-oo0kvp-0 fuCMZC">₹25 discount on 1st order</span></div><div class="Card__BaseCard-b3n78k-0 BIuiq NewProductCard__BadgeRow-j0e7tu-14 MkXrT NewProductCard__BadgeRow-j0e7tu-14 MkXrT" color="white"><div class="Badge__StyledBadge-sc-1o15k3y-0 khwuff"><span font-size="12px" font-weight="demi" color="greyT1" class="Text__StyledText-oo0kvp-0 fxlxQI">Free Delivery</span></div></div><div class="Card__BaseCard-b3n78k-0 BIuiq NewProductCard__RatingsRow-j0e7tu-7 cxqOKc NewProductCard__RatingsRow-j0e7tu-7 cxqOKc" color="white"><div class="NewProductCard__RatingSection-j0e7tu-8 daPCfj"><span label="3.8" class="Rating__StyledPill-sc-5nayi4-0 kwDLgk"><span color="#ffffff" font-size="16px" font-weight="demi" class="Text__StyledText-oo0kvp-0 UKsFl">3.8</span><svg width="8" height="8" viewBox="0 0 20 20" fill="#ffffff" xmlns="http://www.w3.org/2000/svg" ml="4" iconSize="10" class="Icon-sc-1iwi4w1-0 krJKgt"><g clip-path="url(#star_svg__clip0)"><path d="M19.54 6.85L13.62 5.5 10.51.29a.596.596 0 00-1.02 0L6.38 5.5.46 6.85a.599.599 0 00-.31.98l3.99 4.57-.55 6.04c-.02.21.07.41.24.54.17.12.39.15.59.07L10 16.64l5.58 2.39c.08.03.16.05.23.05h.01c.3.01.6-.26.6-.6 0-.06-.01-.12-.03-.17l-.54-5.93 3.99-4.57c.14-.16.18-.38.12-.58a.544.544 0 00-.42-.38z" fill="#666"></path></g><defs><clipPath id="star_svg__clip0"><path fill="#fff" d="M0 0h20v19.08H0z"></path></clipPath></defs></svg></span><span font-size="12px" font-weight="demi" color="greyT2" class="Text__StyledText-oo0kvp-0 bRKDdk NewProductCard__RatingCount-j0e7tu-19 fktyrJ NewProductCard__RatingCount-j0e7tu-19 fktyrJ">29036 Reviews</span></div></div></div></div></a></div>
#<span color="greenBase" class="Text__StyledText-oo0kvp-0 dMKIzz NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja NewProductCard__StyledSubtitle_desktop-j0e7tu-5 kIyeja" font-size="16px" font-weight="demi">15% off</span>

# price<h5 color="greyBase" font-size="24px" font-weight="bold" class="Text__StyledText-oo0kvp-0 BBZyK">₹153</h5>

#delivery<span font-size="12px" font-weight="demi" color="greyT1" class="Text__StyledText-oo0kvp-0 fxlxQI">Free Delivery</span>

#rating<span color="#ffffff" font-size="16px" font-weight="demi" class="Text__StyledText-oo0kvp-0 UKsFl">3.7</span>
