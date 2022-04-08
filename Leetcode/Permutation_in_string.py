from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c1_temp = dict(c1)
        flag = False
        start_index = 0
        for i in range(len(s2)):
            if s2[i] in c1.keys():
                if c1_temp[s2[i]] > 0:
                    c1_temp[s2[i]] -= 1
                elif s2[i] == s2[start_index]:
                    start_index += 1
                else:
                    while s2[start_index] != s2[i]:
                        c1_temp[s2[start_index]] += 1
                        start_index += 1
                    start_index += 1
                if not flag:
                    start_index = i
                    flag = True
                if c1_temp[s2[i]] == 0 and all(value == 0 for value in c1_temp.values()):
                    return True
            else:
                c1_temp = dict(c1)
                flag = False

        return False


if __name__ == '__main__':
    s = [
        ["hello", "oleoooleh", "false"],
        [
            "kuzntqeuvaszrspkgjvxrupwxwrexztptsowceibeewxbslvosbobmyymikdscshybtmanuxeqtanrjekbwirmhgvfmzipfiqxcilarfyasoayepgfzmdytlpjymeaztsyubkbmblepwozffxiitdhwaquozlfmnascomqczrbhxcnzugppddtudxrigfeaozzojpeamnobapgwksudbiwdedvprwonmzardsodhxmkgghqzfhorjaijdvwzsnfpdfklwibbsnwqsoajcpjisbgizgttlnmclawbgnhbmtcpuusuammvgxnopdngclxumgfgwjrinamevhirpmlkwtyxkrmoffrreotdosjghsrkgxyiyrytbbofgczndgmdalyvvoljczcztxitxelywqemjigtuanubpstndwzvtiejtoqvetaehvcuujyupncumjnkesmoadzyvkwvjqgqewvvvpheyyvkewefbjjqzajxnhouodanyruqpzdcjmgnxkmhsgqjhpcyviewmrkfioudzqivmmguxjxuxdmpsmkwnvbxcomifgxqmcovlkooptjpfxjllwtlkkoaayzduodgsusaogswmoqkznynwiukkrrxzkwcknwlazxnlmghybxmyvquzbdqlpfydhnnuvlmyjmixyzso",
            "zthosfejqodcstlqczkndmgwtcakxzxaklkrehkfwnokclametzpnblcwaspdblfoopsiqrpzlbmlysddlqxcjzezcpknwzljvhmqxqinmptcppipifchxexlytleambzwmqwgvxlehnecdqsqbrxqfwvcovgdvtmwbnvajvkizixbmuiuyuixjhiohimghdbohetogrhzsbzgpekosxcjglsrvzenovpjyzknuumpsdrufcjsyfbuwfmaaztxjbpjctnuwcqknnemptjbgfthyafeatskfmysaioqikcpywmefujnvthumyhareltknxyvqprexgbwyzodfkinltwobeukrmpyjkrgvwhbtnzaozgxouxndmkyvzlujhxxwebptykctbojgnvcwhhgsyohccrqxksdyygcwdsazlznhqjdddisjmfqvjqcquuvjrzkcvzpxpfakbkrqlzacanqbggavezedqmoffxmkrlcwxdeosvhvvknqimwpasrlldewvhppzixgcxisysgeppcwfknecupyrrqnkhvessintrequaqiuoesgyndovaqxnlldmdupjcjzejannfjfasguyvgsdakwxezrginhdstbrtqmznpkasytqtbfyftwhgnuazcwehsvcdukuifmkefzabxyhihgnldpsvglubalbsvqstfxehvnpxmrejnkqacafuvzghbttgqmjhqzejasoasbpjirfawcvwahykvrfpaadcgvxssebdznzyvamyilahahgdslwvpuvzsinbbqecdqyvwnucjzyxmxwqwyxbxoljnjcqqdumghmcvqpcpjlxemupospxvkicqvyiavatbojgzurfzitgpeqjmvsgzzqphciyweyavebslgegjcyqmgehchryyclswjequeijzpsvuercqzhwgtgyxhxavhqkrwqdvkqvklicxpasnsnbgybtufdgbwrpaewzwczabckvddtewunsktcznqkivsubdjrpzxtsohiilcybrwqtlfqmjzmvpbfjmbjvbpwietkyzwzizwuiohjuhoekejhmkrooeyydmavdencmxhsxdnyitzivlymzyqogdhzrwhbdupborzqihurziajjwbrfwkzgbpmfgtobkbzyijcgkszyuyouyxvztmmtaqetcaxqrkbrmkzyokglckifgdfidjqoiqrfrpftagxxoqodbyygdioxdznycssxjvpotsrptttrbjayhugecptuibezsyggqcyvzosvmlpwmnuhovvhfyazkdrfxlxjxpbkkbuexxnklhnkteyjshhlojnbxtyltdfzhulcsptinpsskaeowofruejqpinhivlpvvosppxtbbrebvfihmamdlvsjirwfzhzmaqzuryakjlzroxrlwccdannvzwenabvosplnwhotxyzxhocdnvsekmnepzzqjhqrokocqewpihhyftshsfehijlvpajrcrgeqqjigmzkrhcgafqkdkrkkyausijdfzqewawxurtzhioqqnoxhbrdrriveapdebbwbrnmpcakomfhpfrqvzmpqkqucoepjklaqtirgkcrgpdhvyxybnulrchqgbupjdxxalbwljfpdjfnlqfquhdxvvuaecgzgfhulhkkvpuexpssodxqxhrbpzzgdiohxzjxnuhtavlittooxkuededfxdaabuzdlwjhitwykqdvtrwuohpvpgpeudhpslpvxmotibojtgvohqaaowiofdtgbkiiurhcfavlgsnqxndcxyxozklduxqeovzrtwuhoikgpyqoqwllagzufkuzntqeuvaszrspkgjvxrupwxwrexztptsowceibeewxbslvosbobmyymikdscshybtmanuxeqtanrjekbwirmhgvfmzipfiqxcilarfyfsoayepgfzmdytlpjymeaztsyubkbmblepwozffxiitdhwaquozlfmnascomqczrbhxcnzugppddtudxrigfeaozzojpeamnobapgwksudbmwdedvprwonmzardsodhxmkgghqzfhorjaijdvwzsnfpdfklwibbsnwqsoajcpjisbgizgttlnmclawbgnhbmtcpuusuamivgxnopdngclxumgfgwjrinamevhirpmlkwtyxkrmoafrreotdosjghsrkgxyiyrytbbofgczndgmdalyvvoljczcztxitxelywqemjigtuanubpstndwzvtiejtoqvetaehvcuujyupncumjnkesmoadzyvkwvjqgqewvvvpheyyvkewefbjjqzajxnhouodanyruqpzdcjmgnxkmhsgqjhpcyviewmrkfioudzqivmmguxjxuxdmpsmkwnvbxcomifgxqmcovlkooptjpfxjllwtlkkoaayzduodgsusaogswmoqkznynyiukkrrxzkwcknwlazxnlmghybxmyvquzbdqlpfydhnnuvlmyjmixwzsoufvjlrqtzxvybzhurdqdtnkciiradptqxzgrkqgfbnsmptyyggwpenatlrtpvmdpveivmenzwjlwdhlhmmpvbglhxcinvhhcphgklicwwnwqbkbndiuqowwgzdczwvlazndbboublzrltxahxenivmkbwofrnkkvjixfbbctshvqzmgwqrmheupodlrnebsidrbxxjfeoqgcoscymzskvbamtxtpumbdmedjghxazwamkqdrxsqytqxkrrqcnwrtkuaocuwmyucctdnaqfjlosovveoxjyypqrbkflxrrxlnjxhkrrvjettqfzzbwbzowsufxmppazhwiwcvimmlixdzgpmfayrblbkulfopwarxlsbfkuqvhyufwdswfpxqwhuvepyslbliapotofrxhufoopqhqjcjdtleeoedsacpeqfewxehghwvfvqmlzvzudkqxinsfekpbaggbpohbtbhcvdzvuormpzadkhhqqyspfkijjcelofwgkgimjxrkwqwhpqfihyhmwdkwhathcxvxtuopufsjaagbamghtsjewrpooxrprtvqpslsbaijrzojgwhekijtfugwbvgdltgpentcyjbwqjcdqkhicbsdvgtvsecpsacesztkjdskoumcheqzmoijoimnmnhfavttfamkkvugpmnibdzhcieyhhctifhbvqrllslpvymjamfmgladmpeqdrtumbqwcwwkduavjokhjrdbdozxaqemvurjwdukuwrbzfstuesjqfgblvvaqemylqgrtfzdrfgtcbvaokygyidfsbppasppzcunjwbrhqscumnrugeyxqvceninwsvmqcekvuetloevkrntgsrivpebgoobcggmgwkrzagkdavpejdgkpokcdpvncsmduzhowhdjklqwyphevtaugcabxovxgjovvgzksukpnadsblbpnuuihxdkovwsmniptwhrjxhyitozdwgkdkasspklxbyfmmugmawjflmrdiqmolsufpyzkrrqrvgnbtcogomdjrymxgnocnmpsdmbncterfrrxqyrsdqjzrodttnjbblleexyvfzxemlxfmxbzffflpyifrqhbdnwpuuwfhskfevjshsxvhvbldqyxenpxkvamashnbmrfiladqnuzwltrkoegwxrjveajpyvchyotakniwcyigejnaspdfjssacnfhbyobgrovavxoclvkgvgivoiycquftjuqynabeqakugedwlogqfbbivbzisljreuowaxfaugjunbyrcxvlqjvvuewgprwfiofxyzdaomzjfystxrbpmgdwyznnuzibozcjtsxxastlhmjpogvuhdtfhnmrhdxihhrtxqocmsmysxuudsdquadshqncpbejkjarbhkwkstpcqgwuarnmvtfjvdzeeklwnnjdewmwdyzdfnryaqoiysysfvlxetggjhywxwvkvvuccklxptokzvrrhodicekjrffbdjxoftxbstcbxjcksqcvcwkisywdzepzgznaorlllmahrqepouqnrtbhgxnsnyhkacxhjzgvxhlukbvspfzqgguqkngncotvgvuygijtkucvqcsjjolodnbfeznuikkaghyyqtxmtdjchrgybirzkbysbgnwwqaxjsnneazxnmdyzooizcyqtxlmqvujoqhjqlnuvojlkcdybfryidsunirmymtvltnjiggwxeqowcnbukotbngjaidyvhmobdxlklwqxshkaphxwdxzonqddvstwrrtatklpujldtgrofxyunlmlwquruzekmdymzhpuuuaiyinmaedxxhhayzybsepcohcrymkysdaeagmhodvkoissnegjecmtnbydbakamurdqwwgqqfbefltdkdvyldjxynweicudbwirebvzknodfkycidoqaalxorwlvnosvcpudvsiljwlmfqpvwtbjeyydexvfmkiilwlxcpnogyeyspjaumcbrgxkeeezgyrbmtkotoyjnedraupxevwjcluyxdctfazusyqeklxpotczvkphllcgfrykpuwscfknqhfkxdihdkymiqizppipnbflfhduzjgvoehhvtqolybcshofasguaaeaakcsxqsqxpuydzhndleoxgmkrtlivudapfhefocneliicmrtishcmxmcdskyedbqppswqnesziwankobhaxklswulygdojhpobyezjzyengtfulymybqiodmkirqpggycyouzqhrexnntvnlhhokdyzvudgilvqpjkeactaivsjdwfesruusewlpscumpqslulwrhramanthuogjdadmqjeccbutdfexdcsbqujpqdlryelnzvfbncrajicdnomidvmspjljjzglnahdmrctedjzdtozllmmyeamctrcyrzzdzwvfqgjfstbtitgmeogjpgllpihylxgupxxqmheusrglbampwrhtejoqqjkcljmppmemguapopatjkbzomwegkrwxblxgymfmurhfokjkhljtxosxtgmaldrjjhxrcvuddvzlamavxpzszsrfepfsukadtnwyzhwdergrofmetngzuifiuonziduvucichmxhmxrulpykwedymiycbhcsvrkctvqqfvygtlyhlqbrwvmbgnwlryeotjkvowxmdlyjhyvtvyognldmsxqlotfzvxrmdultwbsnstmjakjaqqpfurvwturqyzcnfkoxumuquwgpersslowdvrnssqcgwmfnssvtobdwcscoikoythwhsxswsmsimntribaohzrmjculdnnguchmqgyzqeipuumwgizlvjmpvyotgzmtsantswdarbyaklpiclafgqdaoeiitxlcpwhlqsidkb",
            "true"],
        ["ab", "eidboaoo", "false"],
        ["hello", "ooolleoooleh", "false"],
        ["adc", "dcda", "true"],
        ["ab", "eidbaooo", "true"],
        ["ab", "aaaaccsds", "false"],
        ["ab", "a", "false"]

    ]
    for test_data in s:
        print(f'{Solution().checkInclusion(test_data[0], test_data[1])}, expected {test_data[2]}')
