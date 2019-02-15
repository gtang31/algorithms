import pdb
from tree.trie import Trie


def palindrome_pairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    output = []
    backward = dict()
    seen = Trie()
    for idx, word in enumerate(words):
        backward[word] = idx

    for idx, word in enumerate(words):
        # if (word[::-1] in backward) and (idx != backward[word[::-1]]):
        #     output.append([idx, backward[word[::-1]]])
        #     seen.insert(word+word[::-1])

        for suffix in backward.keys():
            check = word+suffix
            if (check == check[::-1]) and (idx != backward[suffix]):
                output.append([idx, backward[suffix]])

    return output



# test case
print(palindrome_pairs(["abcd","dcba","lls","s","sssll"]))
print(palindrome_pairs(["bbbbbabbabbbb","baabbaa","bbab","bbbabbaaab","abababbbbbab","abb","baaaabbb","babbaaaba","aab","aaaab","baabbbbabbaaaba","baaab","abbbab","abaabbbabbabba","aa","aabbbaabba","aaabbbbbaaabbbb","bbaaaaba","ababaaa","aaaaa","aaaaabbbbaaaba","abbabbbaabbaabbb","bbaba","aaaaabbbabbbbaaaab","abbbaa","bbbabbaaa","bbbaaabaabbbaaaaabaa","aaaabbabb","ababbababbbab","aaaaababaababbbabaaa","ba","bbbbababbbabab","baaaba","aababbaaabbb","aabbaaabbabaaababaab","abbbb","babaabaaababb","bbbbabaaaab","babbbbb","babaaba","aaba","abababba","a","bb","abaaab","babbabaababbabaaba","aaaaaababbbabaaabaa","baabaaabb","b","bbaaaabbb","abaaaaabaabbbaa","ab","bababaaaba","aabababb","ababaabbaababba","bbb","ababbaabababbbbbabb","bbbbb","abbbbaabaaaabb","baba","bbaabbabaaababaabbaa","bbaabaabbabbaab","bbbaabbab","babbbbbaaaaabaa","abbbbbbabbbabb","abaa","bbbbaababaab","abaaababa","aaaababaaababbaaba","bbabbbabbbbbbaab","abbabbabaabbabbbba","abbbbbaabbbaaabaaaa","bbaabababb","aaabababaabbaaaaaaab","ababbaabaaababb","abbbbabaaabbaaabbab","aababababbabaaa","baabbaabbbaaaaaa","bbbbbbbabbabbbbbb","bbbabbabbabbabaabba","babbbbabaaaabbabaab","baabaabaabababaaabba","bbaaaabbbbabbbaaaa","aaaaabaabaa","bbabaaabbbabaa","baaabaaaaaab","ababbbbbbbabaaaba","abbbabaababbbbbaaa","baaaaaabab","aabbabba","baaabbaabbbbaba","aaaaabba","babaaabbba","bbbbab","bbbbaabbaabab","baa","baababaa","abbbbb","babbaa","abbbabbaa"]))
print(palindrome_pairs(["faaj","dhjd","idfhffgcaijhaedadc","dbgcdhjfhfhfaigicfc","cebagfdeiiajaa","fcdbfhajjgfeea","djgeegabijcigha","dedg","a","gdgabgdcgefa","ijigcgdbgebhdaf","ee","jdjbbeddcbeibaih","b","bhhibjjgjdc","ghfjfe","ae","adffjfjcjdcggjcafha","cfabdedhieg","cceeccge","bbg","caifeijjchcbfg","feebcijdgbiagebjefa","icdbg","bhbdg","bia","dhifefcdabgdb","iagcgdfgfhdaeebbfb","jffjffahceggdigachce","eac","dadcfcdfijjghedch","cei","aa","daggbgdhigjjdbfd","cchacjbadejeaibe","ggajabi","chjebd","hacdibhc","bjai","gaehci","aebjgiidia","igchic","fficghhdhcghadbbbefi","cch","biejbaahdiicfidjfaf","ahhc","ffdjgcc","he","fccajjhj","jccabdedieiabj","dcahhdehagegeejcgh","afbch","hefgjcbffghfe","jbadeaggaec","behaf","ciaegedacbafbjjbhcbf","age","jjabadbhchfgjgghibgi","gbaehjafeahe","dhhgjdgiaijbjbgefhha","gaaa","fcbfbibjgb","jfbaeebafedhef","daagaebbffjeahce","igihigghebcehccg","abia","jbfihjcfibgc","ijigefjgge","geiafaegdededd","caadhigjaegbehac","jjjagicgaec","igfefjfhij","cbgcacifd","f","ibbbagj","hjcchhdejdiebbg","eieeaghdbifggjc","jjbdbd","aghdiahf","gfjbgcdheiaahigae","caachh","fahdaaiceeh","hdbedciceafegbjcf","djgcjccafbigidhi","aaehhdh","bcchec","jagcjbagdhcbabie","jiffeifc","gehifhheebae","jbddaeeacecjj","cihjhdf","fhacjbdjaiidaj","iebahehehjefjehegcf","hdjabcgba","icf","ijhfjhjca","hgabdjgchbadh","cggg","ibdcab","ac","cbfehcidebhchbj","cgheeabbidhj","di","ehbd","bhfciideic","fhididi","ibfgcfeiigh","fcicf","fachghiacghdhccfecb","faidijcggcdjighh","hegdha","deefagah","jbbbhfjiaihdghighiab","fbbdaighfeg","egaf","cbjbcea","gbhdfdiiijbda","cijiagbiaiggdbhjb","igedjhbiaijaa","gfjeciidgjc","hdac","ddhjjehffjagaijeie","hhchdcaaijbhbcejgdfj","aifie","gbijhbedfhjbihe","chfijgciaijg","eb","fibbegecjhjjibifjj","gdieddifjahccihgjfde","ceiae","hfhiedjda","g","ciafghacge","gffdjaaddegighfgfcdj","gaibij","ghhhjejachfic","ca","abhc","gjdjijaiaejgfbdibfj","gbcijcbbebibdhafhjih","eegibhbbiaifcgae","gi","ceffbhgicib","fddha","chejedai","fffdciiegheifafbg","gdhdabjedddgjjjediic","d","fhbffgfiaeeghddba","bbacgffgjc","jfde","i","beecdhef","hcdefjeeiie","ege","iahf","jadbecbfh","edfjifjidbahd","ja","e","baddb","jihagdigbje","dedecc","ddahbaihjdabedahaja","ffbiadej","fdfjbcehfheibcfif","chb","ffbcccjjfbbfadiaijj","idhhaecfahifbddgibbc","hb","dibjhfdbafaiif","dcj","bccehbcdaeigabjjib","hacgg","afjifbjfd","ccgeijdb","gidegda","acieihafebicfcgi","faiicicefc","ehfajhg","gibbdbjbabde","fhd","aicifdggfjbeaah","jeegdgfj","id","hahfaaaea","dbgeijffeigdacfjia","ajfbhggbjhchjhagdh","iibiidbej","ehcjcjfbcgi","eadadbb","abbbj","ffjeagificjjcjea","ddjiiadgjajghfabh","eggbgagdffehgebe","ceehieadcejff","caccbacacdgbbijac","hbbjedaceafbbighdadd","dcehggeeghad","hefcgdgdeadcjb","dfj","geccbigghcacgdebg","hfdfaagdfcehjehi","jdacdaaibccbchgjc","jb","dhbdccbechhbahjacc","gcbhddddh","hccf","aihhbfhegfde","c","fheieaiede","bghjajggbdhieh","edbdbehcbgfg","aadbbegggbafh","cdbbhgdjcc","hjfjbajhcjhhjbdicbha","diejiaiaabeje","ebibfcbjcejig","ijieccicgghj","igiddg","ehjfbaehfiaeedfe","fjihi","biehedfigjecchjjga","ijijceibdaiieicaed","feceabidhhbibbgheieg","jijag","ggcgdeejij","fhfjabjjfegfacchaghj","cccaijdi","bbhidfecc","abjdefheb","aaccjgjfacj","egcjbcidfabchhdcd","fieafcjfcfc","egbgdjgbgafhabeie","dgfhga","ab","ggibdfiig","ijaichcihaccibhada","fjjhabhhggg","ediibbhddi","deieccagc","fdiafifac","jadjgaad","j","cjecfb","hc","bijdjgfjbgcgf","highdijjdf","bdcjbaghfi","ddigdegdhjeeb","ed","gfcddeihbaaj","efceifjg","djf","hfggfjcjigbhjeefjg","ce","jibcfjhgadfjijhgijcj","fcigf","bdagehabbjgaice","abfjhcdjfaihhbfbfc","dg","bdgjggdbhaeeg","agfi","abfhfdibgj","heggdf","gceghcghf","aggjhihjhcfaifeh","jidafccbehd","gdgcdehdbjihijedj","fiejddgcjebidgb","cfcijfjbejfbdd","idcjjdcacbggjgff","eih","eifeba","bbeigaiaaegggedj","dahe","jdefaigic","dfefcf","bbcicddjghjdgeeidaja","gifchejfedce","bfdhbid","cbg","dfhihfdj","acidgh","h","acdbcggbgfjbiaacded","fddfhgj","cfgccdeeaebcfbd","fabhdigaiccejibjceag","adgghgceg","ggdeebhff","cifcaadfab","dagedbcaibjfbbaeihei","bfjfjfehfh","dahhbadagieahdcebfij","hgiecbi","dfc","dfcceeebggbfhghhgja","eijaa","bgcjbbdjagcdjbgaeji","faha","aj","dibbabgi","ghig","aijegdejcbhcjba","egc","dajgaia","gjggjbdedg","gehadeabdbicggff","agii","dhbgjc","hiaachecfdjdfdbh","efbdic","debecjfcid","dfgcbjiccd","cgiijae","ffiiagg","fcefcfih","aedifagbcfbc","afhaaacfidh","iejgfggcigcgd","bcjj","hjedaifabgeefa","icdgcceii","fffdacgbbbggidaaih","dahcdfe","fibegidhiaijiajbac","eggfahc","iffciggeffhgig","hcajhihgjjbdajhgi","gijicei","ababgbccgjffdchjdd","ffgecjiafiigc","fbjjdf","igfiijidif","bibfcgbbcefjfah","fababdggcbacjaifi","iaaiijbcadc","fed","hdabhcjidifdcba","jhaefdgfbfeh","jbfjjecbj","abbbacidgh","bdefged","bacgihjdigjffcf","ijbihaejgcajfdcb","agba","ggdiajjbebbd","eighdiejij","cgffj","giihfchggecehgfb","cidcjgifhjabfhef","dihihdej","idb","daa","ddgcejahdc","dhjbghfjeccaccejfc","cfdcbbadibaieifighia","bcbcegiiedfdgbhhi","dfeadcfjdagfdd","hidfiec","gaeiffdcebdcjeeci","fhacgeibe","cdeg","ejcjhdhaieddjdch","fbhiciadfeigbibdcabg","cgejdcbjgbaj","hbagjegecidjabiia","iajjhgig","edhdgdjfcee","aabfibgifhide","jhbjdighihgfajj","gieahieabeaceigbdh","jghgea","cgeebee","icdfaaiiecb","aac","fhhhfjcdbgbghce","hdgefdda","egdiihjjifafgcdcghj","gfidegfaceij","idhghffdadgg","fgdd","ejcaieae","fcadjcdbjhadac","adgdhibef","adhgfhaf","fhfhfihaai","ccjfajcah","ajfh","hjcecgafh","bh","bbiaieaacacfh","ijebgahecfaidefjcdgg","ihhigij","ijiiieacbbffija","ihehifhihe","cbaiebbiffjdh","caecjceieifafa","cfeahfe","iehcehfgd","giichabjhgggc","idacgeibgbih","adajfafgi","ggjcdjhag","bccgacbib","fbggjcfjccfjcjfdjde","fcbfhcd","cbdaecd","jjidajdaadfijgi","jfcgjceca","cahbgjceihg","ficfdcgbjgaccdh","jacgcfiegcd","jajfaeiaghhfgce","dfcgjjhjaejbcbjeca","dahjdfgddbihag","ieegiifhjeidj","bgiaehahc","bgeejdbdjfjaaiedba","hfjjfhdhcefb","ahhdbhdbegdcdcehddf","cbihafh","cgcjfifijjbajcghfgce","djgfhj","ffhbbggdabeibceig","dejiejfgeieedbff","chedj","eaab","ibfhgdaedga","dgiggiccad","jcc","ijjhaagagejicihfg","idibbgeiif","ga","jjcfbegjbg","iadfcid","aheccafdjceaih","eaeaggbjejeghbgdb","cbfjdfbe","ecfegghjhcbgbcbciie","eddijfbicdhce","cijbicdgedejd","if","hfebih","jeejbgfcdhhf","cddhfhg","deaa","eiechie","gh","ghhiaaddbjbefj","icijhcfcffjheeji","aajfjjeefjfbcgfgc","ijajdffahb","cifgbcjjgejag","aifjehjjhchcfcgd","cebdahhjbccfib","jg","hcie","bjjjaf","bgbibefaafcehc","ahcbaebh","geaeddi","hhb","cedcgcaedegfbfacbbij","iihfaaich","eaecibgadagjdgge","ehbfaicehcibaabfggc","jeabbiaeh","hhcach","cjjchcdch","jdgbfgcecagd","aea","chhjhbfj","eadibff","hccgjgaabcabajgahbbd","bf","fjd","affhhjcgdjbjcgjcb","hhbej","fijfjhjifbbeigg","bhdjhfebdgiggdeici","eddcagi","ddh","gjjddehcajgeh","ehdjaeabgdajjbeabd","gggihedg","bajibfeibejbea","fiaggibjjgficd","jfhidccgdfgahfh","heafhcdigeifhbaegae","hffahjaiihafhaaf","gcegdddgfbb","fbedjbhfbfhhfaejcbj","ddfhghfbd","hejejjhdbbfieejdjdbc","eigbichggbeafchd","dgcahcjfjfgi","dfbiafaeefbfia","ibca","chaidcd","gaheaijbhfhjhfiid","jihgcbfef","hchcgf","hcbbdjehfdaagjdef","eha","caif","dbcaijgd","ihabceadifjc","hfdj","jcahf","icdiefgje","ibeiehbejcaiicgcajaf","ig","adfcf","chaghcgggic","deedcbb","ibjefhhcd","ie","cbhbbicihabhf","hjg","gbdccfhbcafccbieafce","afcfe","jgb","dghgijiiebag","jdfhceicihcgidggee","ddaciehfjaediggia","ghfgidghb","cdichich","hhhbifffa","hhfdhjegfjccgeedjb","dahcchiidicfeagiefie","hd","gibhidfjfci","edihdgagebdbc","fbgdjb","cbfjhjbbfifcafbafid","bedafijjcjjfebggb","ieccgeebfcbhagifeg","iiafhbbjhighef","gfgiiadjb","dgeeiaefc","ebdbc","ibidehficicijcij","eedbe","idhccj","jdaiiba","bcgjd","jcede","hgddjedfcadej","jigca","hgbbf","gcjbjibfahgaiaij","jfiecdeg","hbbecgcchhhbhchdhdi","jefghdjieedhbha","aggfaiebgifiajf","jciiifafchjjf","iicfdbc","echgajhibcdhfccdhhcd","hfaaifbdb","hjibifhhfbechbhaeji","efhjg","ddbchahcijjfhcjedfhc","ffg","ibdaidadfaa","gfdifaiiecd","fciihhebcjdacfjjia","aifdbcjjfjaidbhh","ahg","hhghfj","bjfcgegi","bbfibgbiicghdbeabbai","ffjhig","dheefechicecid","fggcihdeda","hfdibcdcgibcfhggeh","fgjja","higbijafjcii","ijichhdiehg","hhebcd","jjdfaggbdegb","aiegibdcgcb","aajiegb","gifehjiebdbacjf","ejgdhgdadei","diighceeehbb","cigffddgggeahh","bgfhejjhia"]))
print(palindrome_pairs(["c","ijefjehefbeabhhhaadf","jjagh","jgffdcedgi","d","bhgdfcdcghb","dfhajahiajffe","jjdcjbjgbbjjb","hdfhfcaeiiejaih","ejheghchjdfdi","ifedbjgigcfai","jhbcjj","ehiggi","i","dcbhc","bafccbabge","ejechhdcaecadiaei","jaigade","gaggihi","jajaj","dhijc","j","ifeajhj","icg","gdhhedbehbdbefgeaghd","fbhdagdcgfabbbedeh","cajebjeifchbcfghihhc","hbfgehece","jdfgajbicgaaj","bfhca","egfb","gbheieahcbhcijchf","ggghegajhciae","ahhiagjfgecjbfaaibce","eeedgba","fceegjjdi","hjdeehhddbbjdfhga","fag","fdedgehj","ifdbdibbdhaa","hedebdicffhigajh","dddef","gdgefgdaiccbdhc","afbigedbga","fdcdc","haidijbcefgcehgch","bdbegcfehbdjfi","eahcbhjd","fdhifigghfffg","bicgi","fbgfica","gi","cfiiicbgjhbihb","hdad","igfefdahdedebfh","dbgcfcdfgaieiegfic","adjeibihjiii","echibfjjgdbgge","h","egb","jfgbebggdcjjhjebj","ag","fd","dfaajidiejca","ecjijbcihafcbc","bfaddg","gdcbgfecfegahfeggigh","gc","iadaahghcdff","fhfecefiadbhggad","dadiacegbffdj","egidaehijefg","bfeifdjhcffdgcgb","dabeffefgb","iah","fcfcgegjiacdgc","gdafcdigef","cfbbddafifjjjaij","bi","dhdbfihh","djaeiafgcaabiedcdg","fbe","aagaaaf","beafdhghhdceifbi","cicigaabghgdjj","febaebhaeebj","acahcjjegibgg","dedjbfjhfjagcfaie","cfecgdecdedbeghjdjj","abjaeaejie","egeajchd","defihd","bjg","eceachhed","aeihjjffbjfdihdcigg","fghgjabih","djfcibdeaecbcdigahf","eeaeacbifcfcb","ihfffgaahjbfgaijf","afcicff","fjgihbghjgjcg","biaiigjbaahaejgi","jajhjeacieg","aabjgahadheebe","cjdgaeidhjhcehahd","cgcgafgcdga","jfabcfjifjabdafhh","dhchjcj","fj","cddhjbdg","cgbcc","dhbicdhghdihbii","addjadabdecchaahdhj","bjeehfbihjacdj","iiehebdccdcfajhff","ahdcjecjfhebaigf","fh","hf","idhachdcccea","ijhgjhegegehch","ajaajeeicdigjgh","edeadfbbc","ech","hif","bjdghdhfjefghbdaece","diidbiafg","aaahagibbhjgjahddg","agdjhbh","djbjgghhjijffiefi","jajihdgecajhibfbj","daf","igdcdfeiaeiieifegi","diaaghjfdjiffijechac","da","edfdaebaibaijaaj","igcbaijca","bebgifdbjdfdd","gjgjghccgca","deaiehhhihgf","ib","cajddibhiiibjaibjff","hhgfbebececcedcbfha","cdcbgaeefeejabbhbg","ajhbhcjabcbegb","gfgjeiihhdhhah","bicfiigahciecedigicc","di","fgaeeicgb","hgahdcgdeefgc","gcgche","eiheib","dgejdcjegdb","baeheiij","ibdbjfjhhgicjijibi","bijdceh","hiaffag","iegejfjjhgabbbdgg","jdbgigjfhhddi","fjcaedecfihfhfca","giehgf","gfe","aiebfdfcgfacjcebij","ghedibbiecbebccfbefe","fjgihjgcafdaddje","g","dfeechbfdhjebddd","jheefdagd","jigaehiehcfd","gbacidgfcgcabgjhjb","ajcegadgcagaejfjjhdd","faceehfdeebbigbhg","agheegaeifagjcbjjejc","fhcgidcjaeahcfbcdaij","bhajejbgcij","bbbe","dijfacge","hbigdhbbeijdjgadig","iiecieaabfeghdc","dhbaicdgfb","hdijibehjif","hgfffhdejddgjffaff","fc","ica","hhegihidgbcijjbij","ibeffhhchfdebdfca","aagiedadddhdejajb","bffbcifiibjcbfd","fjjjhdhjefijheafgbf","iahiigcidaf","iecfccihiibbddiabhj","hg","fggihgaedaaiifhhfeh","eegfjhg","gajia","bdia","iefffagahgi","igeeafdibegijicjc","bf","eedajefffggbedigehhb","djedahdefbgdfghj","ghibjddbbbggdfeihedb","ihghjgjecacjg","fgheicgeifafidfga","a","eah","jccbbbicaaddefj","afaififfdaaihbdj","iffcccfadiabjddef","ahffchhagfjjabci","jjfajdgjddddhhebc","cjchc","aiahhaf","gjbbcbh","ggfafdehggeh","bd","ibcjhiebhhbahdcefbj","dg","abiedhhjeg","hbbd","bg","faeffciccebjjfhdd","b","iiabhjajc","aideadfigcdcacfg","affefjdjgibcecdjchbg","jibgigfgfdeabcbhdd","fi","eeeh","dhchhdgcdechi","fibbbhaiij","afijbehgbhffbjbgbhf","cgcibfhhe","befdjd","ahccghahfeeb","bigabeaaaebiebdbfgch","eheiib","iedccjgajehh","fjfjjdbiihcidjddb","ed","ibjcdb","ffabbj","gbhhbabcbbaieahgj","cededb","chhhidfcaifjigi","eabfjbihfdhiabffg","hec","bfcfdfgbhf","dbfidjeiga","cbgccgadg","difhaijhbgbeciaabi","caiiffdagijgdaachije","fabcjcibbgb","hfcbhahcdccfj","echfjgiedehg","geicejjdhfbchd","bfe","f","jcfbjecjaj","ifdh","aiijhifb","ch","afcbehh","bchffh","cdeh","fhijgej","fiaa","fijfgcdcaajheaa","baggdffjfjaf","jgbeajajaidicb","hcjhfdggehcagjddbic","ijach","ibgcgcahdaijde","aebaijhcj","dhjgahieddcf","ehfjacabdge","fhjj","gjheaahbbjed","hegahifhecegai","caehiibff","ffehhjaajhh","cfd","bihjjeijaghac","hffejhjeadjidgj","chdfihdfa","dghj","jfhb","cbecjhgcc","gbhaibedghjjfi","eh","jjcaj","jjbjdhgeicadjja","ahaehidba","jdaaigfdcahigdf","ieihejahabgacc","iggdbfecbgcjf","idgeheeaedgbf","fbgdgefecjbbbdbhhbh","fda","cifiibfhdfcjaicddhij","hcfdhhbchdcaje","dgeacjeaigjgbegjbfhi","hd","cchgeffaiceidiibb","eebfjgabcfchc","dfabfdjj","feeifi","edjggfaf","cgddaddfhheijcf","fdefgca","fhcj","dddahjghiejijccdaf","hgcighbbj","biigbgcijgfibja","bcghjdhabbffijdhddcf","jedhc","feddacadhcjecacg","bejfdjegfcfjjacjhcc","bbcbhcfj","ehibfiieicecjehj","bahgeihcbacj","gcfa","igd","ahfhfgdf","jhdj","cgad","acjccffggjbdgdbj","fddidiacecdbjhc","eifeifiiecdcbdfbc","ejddjadgehjhia","hcifdjhac","edffjcfjhiaidffhf","eac","he","fdjeb","fibhjbaeghecdgjbdfc","fbeeccecaegaiaebhija","hehigdcegeigi","ijgfiibchddb","jgi","diebbchbfcjdbiigajdd","ifabigaiijaaiccc","hhgjbcaeahgbei","ghjjghbheghjjb","jdjhaaedbgabcgcb","ibh","ieaecegjbjaghbjdab","hfabjfbaabcjjaejiigh","ifdjgggefeajgdaeega","egfcdahgbeiffgdiji","iceefiahfaej","degjfecaaibi","eihfiea","jcgcdhbejhafiddgeghg","cedjagdfecfd","ieegaehejhbcgjg","hcedcgjccajaaahfbbci","ibdibeejcfjifigb","feji","debdbbcace","bacj","agdgjggfji","ciifgjgjgacaijeffh","gaeicjbhbfcf","e","ehcahedjbe","ahaahacijjbi","hbfhe","dbjfjcagccajbeeaf","jeigeieacdacafe","cgcihhcjcbbh","igbcccfadgach","bjgagaceegigfecbhj","fgbja","iabd","hdac","fibaidcfhffejg","hda","eehbedefbgij","dddiidhfhdchjgfh","gcceccicgficigbbehee","jfehfefhigifehhdce","eijgdgceigieaagid","hdfhiigehibffcd","fcfdiahbccjgjfdfd","iadedbdbafejdhhdjfe","ggfhhdhcdbceffcehhb","ehbhdcjjdef","cgdafchffajjeidc","iijhegfgbbcafjfahe","ifheei","be","cdhbiefgj","ihj","ajgicgeffdfcfhfgaif","gfgdbi","jhchjgad","hhihjaaagig","chacdadbceacchg","gcacijcdjfaf","fadgccefcfhigjh","fidbe","gcch","bgfiaicgbdgefjga","aehjjadagibhbjbejh","ajefhddchggjdbcfi","bjdcgaachbjdhd","affadiigjaddde","fihhfbddfg","eceegibdbfedidcied","jf","aiehabcjfiggajgbeih","cai","jgjj","iccdhfbhj","hebjidafffieeeggagaa","bdfdghjgbgfbad","fdijedba","iccdjcc","cbcaehdffcggggijdb","hhbbfghbhjcggd","facefacjj","idcfhfi","ffagfgaef","hhaejceacgbij","gbfbfahbghjadedijcbd","dbi","jdc","ebjc","jfjehdji","ihhd","jjdddjfiaci","dihjaf","ahfcagaegicfeg","hgaaha","diefia","ajgifhfaddifigigcaje","ccaig","fjdgjcbiaigaad","giabbcfbbe","hdedfjfgiefcgahajgge","cbeghggacgc","fhebgd","ejehac","aifdjbidfcdeeiab","ie","igfdcdhffffigagheije","hjccdj","cdeijcjhidibifdj","dgijh","bgdifadhdhdgcjeiihe","ddhfeejjciaeb","debdjagbcihhccjbb","ffbhciehjbgfhhdj","dajfcacdfcfc","bibfg","bdhbbhaedfdaa","aajdbddabgbh","jdgjddf","beiacajegggfa","gfffbgjhe","gajb","ibhbcdje","dfagggdcdbgifcdieih","dcicahgadeejeigfcicj","ai","db","jafhgg","heidfdcgbacchejc","hdb","fhedhhcfgdh","ghhjihjif","hhbhhgji","hgbhdccjgfjgibaigj","heiehbhdchai","ibhaeigdifcafeci","ggcfgbibab","hfbcejg","hhdg","ighdajfceaebcca","eahab","gadcegecefddjhajidd","ecddcfbjdije","hdjefaiagb","eeccfieiihhihbdda","ccgd","ahajagjbehdabj","bggceegi","idih","jachfgbebic","aibidgcb","aeagfgjgbhh","iegjccichbh","abhhjaeiicfhijaddij","gaifcciggegijhhdje","fagjiiaadigifjcef","aieddcgieddbicaid","feb","fggbhfefjaf","dhhcjhgjahhgbigbefb","gcibi","gbie","hiiiefgdfca","acjafeaiidjjibeegc","defbgabh","hfecfdigijaid","jbighafhghgfifbhajfj","deibaajif","fehccjeded","ffedcjdfjaeabg","hjdbbjjfcjiadefbbfej","dfe","agehi","dadc","jdhhcfcbbgd","ejahicjb","abfcjjhgcjbhbgie","dcicidgigd","aifhejbfffciheheaae","daeabaifjhiidbge","eaid","aifeeh","gbiefcfjhghgfhgje","fjchjjefhe","fdeeeeh","daefhifd","jhbedfffgjcgaaecej","dccddhdhjhdcbjecg","egfagbhifbchjjaejibi","fiefaagabdgabghic","ahifeijihjcghf","dgjaiibfi","jgijhf","jigfceajghf","afceaj","djiaidaggbgaegbb","cceagfffdg","jfccgjdhjgag","fcfhfahgefjfcijjdie","gdjagcgjdhijjdi","badfdfeeeaji","hbidiagabdafhdf","fejdafbciabf","ffidgbhihieeh","cjihdjchdchjjiigcbg","bifjfijjbagdda","cjccbjeigfjchdjjdf","igigaacdcgcid","jidjcahbi","jiheeedeaibbje","iace","ijhifdibcfjdjhddecif","jjgfedjgeieecfi","aiggcdhfbdcc","iadfejbghbfdffi","eb","cjjeghjjcjg","hbdgjee","dhdbccgffddhgbh","hgjhcec","bcgjee","cfgigigjahdcaa","ahhbgg","eedhjfjb","diihgfbegadb","jhdedaijbjgjbdbfj","fhgfg","ieahdbafghe","bdbh","dghbibbeijfji","adbhcjijahejchabehbg","gigbj","agechc","jaegffbegidgbbfhchj","aecjb","bghjbbabbjhhgfabhhj","ehhhh","eahdefegejejhihhichi","iegbjbigejhgcgd","idehbbfjdfeegeii","acfbjdfhhcagjbhcga","ehfh","eadgcahgajbd","jbidfgcecegeej","ageg","ifj","cidijiebe","acaaabehhcjhehjfcfc","cehjaghfbegha","bajieadjfcgaicijee","aeicjfgbbeagdda","ieijcajg","gbehd","jajedicajaecdbaaih","hdahe","ddbfchhicbihdaff","ageei","ggcah","egcgieccejfgdjcgbc","badhi","faafebghfhgiafdaeajh","cbhdjdaaaaffefeicd","fciaggejbidebcfb","eecib","didfciihjgbgcfbe","dfjgf","gbggca","ibggjeh","bbahhb","agcc","aggfeehjcbgddaabf","jdhafcdgbafcdgaacba","iebchhcijbdh","dbehidccibjggaegc","df","hjjaefefcjfb","igfaadba","fhgbdceegd","iebfgbhdedbj","jbbgdhbbfidihaie","ihdcjcgbbecagg","cbgdfjgiaajbjbjgfbif","aajidffajfgeefd","jjfiecafjiegadjficcf","eeficdibd","jdgeed","cjad","bigfbfighgijaeabfjha","facgc","gihhahhdfifj","cchbdfgdbcghgfaaae","aechehcfhegcedf","jgbfdheaf","decfjfefadi","faha","cgfegd","dehcafhcgd","gd","bidaeibgj","hgfegbjhdigibgh","eififfabcdejj","fcabgbcjhfaebace","haehedbjaj","ccibefffbbdfiifcih","gbdgiaib","fchicfhdaiahagcfhf","hjgfdejedjhjfeed","faiijjibbjcab","ihbeffba","ffbfagjhegjfbgjedff","ihagb"]))
