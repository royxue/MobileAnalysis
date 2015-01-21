from pylab import *

dict1 = {'ce7bd488-c03d-4613-b89b-34f3c111e889': [1470, 86357309.0], '2a44be79-a397-478e-8cbd-491defee4507': [391, 151889945.0], 'f681b5c0-9af0-49be-a174-461847514f3c': [555, 40476120.0], '6665b446-560e-426f-ab3f-e8727822b80b': [29, 253199.0], 'eedb78c7-3fa3-41c9-a0ff-e435a80cfd49': [30, 695291.0], '5f85a44f-fd53-4544-ac89-47b9d0b9050c': [1825, 644189263.0], 'a37e0add-0249-484a-ad12-574fae796ac2': [28, 578258.0], '954fb99f-ba6a-445c-bdd6-0416e4868f77': [132, 3887695.0], '0292cdba-85c9-4dc6-8b9e-079f15a49a3b': [3724, 3117964544.0], '98a2b05a-f11b-459d-abf4-ea559609515b': [362, 572356492.0], '4af8a837-1d5e-4e77-a252-5562162f3467': [28, 1984647.0], '54b8151d-3b5c-4515-8682-d9ff41ab1c5f': [1555, 1118879015.0], '20bf17fd-aef4-40eb-99fb-b63a43fa534a': [865, 1558109735.0], '1dfc5843-a0c6-4358-b9fd-eecb18798e3b': [3079, 796003513.0], '0f7c41ec-4159-4fba-865a-d2696dd2c6ef': [3054, 2189831428.0], '2697121b-b81c-48aa-b133-e097208b2b42': [787, 361905988.0], '13b7fd6a-c6e0-4635-b719-e29760384324': [308, 65547994.0], '8f66ced5-7a89-4e6b-9e7c-b1f2813d16b3': [1580, 1909515517.0], '4ec8fef2-cc3e-4f95-b2a2-a5de08c28207': [600, 120109552.0], '851ea925-ab15-494b-9b03-037fdc88569c': [3431, 1214743737.0], 'e71b7c1b-b8ee-4c0f-a608-532a9c461577': [870, 48910179.0], 'cba0a7bb-455d-458b-a98c-56c861cd815b': [23, 594140.0], 'ab5ae194-dfb8-4b49-94d1-9b17cf8e94cd': [1288, 818945847.0], 'a77714ce-46c4-4332-8e17-bd2290b5c684': [898, 222821822.0], '577aadb3-1888-4b98-b8a7-90a56fd11eb6': [1, 6803.0], 'e91eda19-89cd-4b90-839e-ba6afd1d5b06': [346, 93104962.0], 'a630ca85-bd42-4315-acf2-492763ca72f8': [956, 1289394918.0], 'ee840f5f-e0fe-4a43-8202-6dd6c63ed0a2': [943, 341856284.0], '6214d163-4333-4334-82b6-50ea6bf20b93': [6580, 1224134539.0], '08bfeec9-dfcf-4cca-ad46-7bfcbe26e5c2': [216, 74015948.0], '422f9ff0-d6bf-4803-b66e-b92dae8c374a': [134, 2151329.0], 'e6be4c1d-a386-4a60-ad54-44b866f9aa46': [144, 32370870.0], 'd1a69dc1-6113-4acd-93ea-717b03a4768e': [1016, 125471557.0], '99a054f5-d2f5-48ae-bcae-f42c9162cf75': [157, 118808135.0], '99b19045-09df-4aba-834f-ddc4932f9923': [443, 104412041.0], '4ca035e5-a040-441a-a298-384c176c3f74': [750, 85205427.0], '8a1dd46b-bf8b-40f8-8e82-e4e63c572607': [71, 10152809.0], 'ce09776c-d36f-4bc9-818f-dbf38c17b553': [2366, 988570527.0], 'aaa821ff-477a-48fe-9c65-86c394d038d1': [4, 181303.0], '544ef295-33ea-4dad-8eed-2d1ca2d1112d': [1562, 513547922.0], '03b71f3f-2a39-44d1-a1d3-f66cd6b2eb5d': [468, 58259141.0], 'c06905bb-e022-4353-86cb-1dbfe1d33967': [628, 89285782.0], '41c843b4-adcd-4c25-a450-e574612e295a': [3316, 173211212.0], '64a134e2-b105-4125-930a-d2b0732cb7d2': [37, 1269907.0], '89a66a26-3538-4ed2-a951-7ba902b11407': [2360, 224782367.0], '9bc16932-5446-40bf-8011-392cc6d83906': [8317, 434936162.0], '0c030ede-4ebd-409c-bc76-344d5a08dadc': [3313, 9135422535.0], '86f968cc-27cc-4e06-85fb-f4296cdf3d20': [2668, 711237989.0], 'ad0a7209-4d8d-4549-8ee6-0fca2b5e803c': [1667, 74173228.0], '2eef50f3-e540-47d7-b9b5-8531695b4a2e': [947, 86584668.0], '9236d13c-7f8b-4d63-a83a-02a09ea18ae3': [2, 10492.0], 'cc4d2b00-0fff-479f-b0b5-3ac5ad05c06a': [1, 4117.0], 'f3fd3395-ac57-4902-abcb-e1840795f4be': [10, 395541.0], '77b434ce-18a8-46d4-80f7-0c8b1381eb06': [2929, 323506922.0], '3ff62f89-d91d-4cc9-9c0d-290944531ab8': [115, 43074301.0], 'a9afa150-173a-4103-94a5-f34797dfbed9': [2587, 384941183.0], '60c73dae-4a7b-41b8-a228-c2ea91b7dc79': [73, 19620211.0], '5fc40d77-7167-490e-9e4f-3c1533547a6c': [1340, 96309650.0], 'b509fbbc-eeea-43f6-b8c0-53e82b70aeed': [1045, 295762861.0], '9a9be2ac-ff80-42e4-9e12-14345dc5a458': [53, 58287632.0], 'aeb5b1f2-f6a5-45e4-abd5-f75b982415b6': [329, 7156544.0], '742825d4-10af-4f3f-9266-3bbfaab58164': [92, 2569039.0], '2bc7baed-7e94-4759-9bc0-e73fecefce82': [51, 2118591.0], '903459ba-11a4-4af5-88c7-87ee637f784e': [95, 8622771.0], 'a18b5945-6c39-4d19-b216-7192b4e0b929': [602, 38532558.0], 'b179b5f5-f180-4052-892e-698dffc10545': [120, 7056843.0], '113211a4-1e96-4168-a0e8-fb205a367271': [109, 31075937.0], 'e6e0dfec-1415-4b16-bddc-74add545cf67': [8, 84454429.0], 'c069777f-825e-4516-9cb7-47b5bb4e62ee': [2166, 1107674712.0], 'c26e96c6-2ddb-4287-8bd8-2e8427aed950': [821, 193346893.0], 'e1ecd267-9982-4107-b3c7-951b9e90dc6a': [891, 300909900.0], '83d9dca1-d698-4453-bda3-f3733ef8d406': [501, 695227006.0], 'd632c816-bbf4-4d66-9413-4b4eca63c57e': [59, 1284574.0], '3a82f670-630a-487c-8449-0603c288d7c3': [911, 312437022.0], 'cb980575-9077-4f39-abb5-091e458dbd28': [1076, 44426978.0], '33ea8037-8052-415a-87cb-f6c6e12a4c52': [3413, 1555642317.0], 'f31028e9-303b-41f5-841f-b3fe990698d4': [728, 282137252.0], '251c72dd-0cf2-4b20-ab82-2e78e806f273': [340, 452981484.0], 'e584ffc0-5f9e-4f61-9810-670d1e49e901': [9560, 2260273166.0], '9129d6b5-9d52-4f0f-8298-3421dbf2a359': [320, 132947831.0], 'bc47989b-c288-4de8-821f-d11f227e3e42': [4215, 619505492.0], 'f1650b04-88a2-486d-a3bd-012a1d390050': [429, 249802265.0], 'e9ba6a24-5e7b-44f8-8b43-a71f92e8ae04': [5891, 2295752080.0], 'a188c493-be0f-4441-8ea9-21f1384b7f0c': [152, 8332134.0], 'd8f6890b-fa70-4fc3-8093-63eb264e3642': [449, 402206808.0], '3372860e-b042-459e-9dd7-77c8cb2de4a1': [1255, 270022745.0], 'e7fcf2b3-844c-445d-bbb5-3d6490457abe': [1444, 45822743.0], 'b3b6f59d-002d-400f-ad2d-27b103b3f3d2': [2033, 262211538.0], 'fc87af94-432d-49cc-afc0-fcfc2203f48f': [1857, 379339295.0], 'db09f576-1fee-4c9d-ae5c-2db25bb05cc5': [269, 23997447.0], 'b1cea15f-37f6-4c77-b9e9-84c9eb5efefd': [1658, 639807336.0], '22a4ce30-ab29-4c8d-9b3e-e6da26fd0a88': [1343, 239540225.0], 'b51420e6-ba0d-4539-839c-89d3684149b5': [719, 360979374.0], '6c0116ef-3883-46a9-8e68-9e7f5d96b79e': [1672, 215492323.0], '7f09cdf6-5bda-4a4f-ae9b-213adafe406f': [114, 410656566.0], '287f03e9-08eb-485a-80d0-34defb5ccf75': [445, 210580799.0], '2d5ca692-eb38-4b64-980c-8213b85ed008': [430, 192461423.0], '7cda5924-c0bd-478d-904d-a390189d6432': [390, 24621620.0], '49ee9333-9e87-4ae8-817f-8d3c05d341d8': [33, 642775135.0], '32db5f39-25bd-4376-85b5-fb93d78d3353': [127, 28561851.0], '430c4ce9-2e5d-4db1-a311-3132171dbe05': [17, 1764245.0], '2bb69ee4-0d81-4189-9219-2c86a7eb8ca0': [180, 305079066.0], '87f195cb-4975-49cb-961a-ab36e986d45e': [368, 32976079.0], 'f546693d-ce5d-4af6-8dbe-0fe090954ab7': [333, 89164988.0], 'dda31ab8-d40a-4b7b-a659-9f4cc23d98e3': [876, 154436731.0], '52f9db4f-fd3e-4928-b7ec-d699f6f63952': [452, 173328978.0], '947e4d15-672e-433a-9270-b53c9d7ae46e': [336, 174274377.0], '9f322df0-1652-4c1d-a91d-2c8834a2ad71': [1088, 624179461.0], '6d90be1a-0af2-4ba5-8296-ae91ad9efe74': [4, 92018.0], '4982eeb0-9938-4288-852a-c5c8d759666c': [73, 3047185.0], 'c2e3746b-ac3a-4b91-923a-895c879cef29': [110, 5453625.0], 'ee4b89ff-546b-4e71-b6af-dee9ac521a08': [395, 25692953.0], 'a7870283-36a9-4c8c-81c7-ea65f56c19d8': [261, 229211347.0], '7dc470ef-90d7-4d4a-bcbc-860a3d1da445': [1233, 2154934685.0], 'ac32d7c5-e84c-4f43-a356-fab68c06b507': [317, 6981194.0], 'd627eede-1b7b-4876-ab25-1ff42ae0280f': [865, 197532861.0], '8873d812-5403-40e3-866d-d439b2711b0d': [694, 176852764.0], '8132cd26-fceb-494b-91f4-433560176116': [1101, 382214273.0], '0f155df6-1f6b-4e9c-83d1-d4452913a071': [479, 93784909.0], '9cd1d472-4147-4d9c-b0d6-fc5f2b07d7a5': [91, 1800105.0], '07a17b04-2d7c-4ae0-bf37-f3b1ae7ba047': [445, 18544886.0], '6a4d382c-8e5d-4073-8a4e-73b03309f840': [310, 31630030.0], 'c3ef90b2-e046-4ccd-ad2d-46bef42d5686': [717, 89375111.0], '94d19c72-a97f-46b2-b31a-7c8b2d904a79': [3183, 819475915.0], 'bf0ccba7-e5c6-4a0e-80d0-1d83533fe3f5': [693, 67953959.0], 'e83a3f24-5e1c-4d00-bb25-4672ebd9acfb': [843, 201821873.0], '78f47549-3ae2-4bc5-94e3-2684939bf130': [87, 36270420.0], 'bbc2a616-e3ab-4630-818a-264841c7d0fd': [1028, 318339270.0], '3d99afaa-abca-4d29-9a2f-a5c49e22b5d1': [1005, 138110808.0], '4c98c501-fc64-4767-9305-40eb2af22410': [13, 446604.0], 'c1f13036-8d17-4660-8753-9dea984396a6': [1, 2123.0], '11227db3-f2b3-44ca-8bb4-cc20ba7af6f4': [116, 232210736.0], 'afbaec11-75c4-48df-b43c-3878b3359a04': [338, 234520495.0], '7e3582ae-34c9-4e06-a28c-2fd76d881ff5': [4468, 1038894952.0], '6d4c24e8-80ae-4d0a-a24a-71fce85098b9': [2726, 772118653.0], 'f9a8edcf-96d8-471a-a435-9b7d3cb9cdb6': [285, 33200766.0], 'e2036160-73f6-49a4-abd3-c0c5bf094733': [64, 38648027.0], '35cb8808-4742-46b2-b9d9-fa15d73391f9': [853, 319764545.0]}

len1 = len(dict1.keys())

pos = arange(len1) + .5

val = [dict1[a][1] for a in dict1.keys()]


figure(1)
hist(val, bins=50)
gca().set_xscale("log")
ylabel('Frequency')
xlabel('Total Duration')
title('Total Duration Histogram')
grid(True)
show()
#savefig('Duration_usage_per_user.png')






