


# import random
# english = False
# cn_count = 1
# en_count = 1
# all_list = []
# with open('a.txt') as fin:
#     lines = fin.readlines()
#     for line in lines:
#         line = line.strip()
#         if line:
#             if "Zhejiang University School" in line:
#                 english = True 
#             if not english:
#                 small_lines = line.split('。')
#                 for a in small_lines:
#                     a = "[CN"+str(cn_count)+"] " + a + "。"
#                     all_list.append(a)
#                     cn_count += 1
#             else:
#                 line = line+" "
#                 small_lines = line.split('. ')
#                 for a in small_lines:
#                     if a:
#                         a = "[EN"+str(en_count)+"] " + a + "."
#                         all_list.append(a)
#                         en_count += 1
# # print(all_list)
# random.shuffle(all_list)
# print(all_list)  
# start_id = 0 
# end_id = 0
# length_list = [1,1,2,3,1,1,1,1,2,1,2,3,1,1,2,1,1,2,3,1,1,2,1,1,3,4,5,8]
# idx = 0
# while end_id < len(all_list):
#     start_id = end_id 
#     end_id += length_list[idx]
#     out_string = "\n".join(all_list[start_id:end_id])
#     fout = open('messtext'+str(idx+1),'w') 
#     fout.write(out_string)
#     fout.close()
#     idx += 1 
    
       