Title: Šest es v přístavu
Date: 2015-10-18
Tags: pelican, html, static, ingress, javascript, pdf, docker, compose, devstack
Authors: Michal Valoušek
Summary: Tři lightingtalky (pelican, ingress, pdfmake) a devstack nad Dockerem
FrontImage: /images/31_6_es_v_pristavu.jpg


Na říjnovém tkaní jsme lehulinko zaimprovizovali. Zdeňa musel do Bavor (na
vdolečky), a tak jsme díru po jeho javascriptovém výstupu zalepili 
třemi ne-až-tak-lighting talky. Druhý řečník naštěstí dorazil v kondici, takže
celý sraz dopadl namíru dobře.

Jo, a klobásky v Gobelínce stále mají.


### Pelican

Nestýská se vám někdy po starých dobrých časech, kdy webové stránky byly jenom
prostou kolekcí HTML souborů? Pro jejich rozjetí nebylo potřeba instalovat (a
udržovat!) databáze, skriptovací jazyky či nejrůznější podpůrné knihovny. Stačil
prachobyčejný hosting s FTP přístupem.

Určitě jste sami v posledních cca dvou letech zaznamenali vzestup statických
generátorů webstránek. Jejich princip je vždy stejný -- do předem definované
adresářové struktury umístíte obsah (textové soubory, obrázky) a ten pak
jednorázovým procesem převedete do HTML formy.

K čemu je to dobré?

Spravovat obsah touto formou je blízký běžnému workflow programátora:

* obsah webu udržuje v adresářové struktuře s pomocí svého oblíbeného editoru
* změny v obsahu sleduje verzovacím nástrojem (Git, Mercurial, ...)
* v případě že na obsahu potřebuje pracovat více lidí, využijí pull requesty
* pro překlopení obsahu do HTML stačí zavolat jednorázový skript, jehož
  součástí může být i okamžitý upload na hosting

Je jasné, že pro holky z kantýny tohle moc není. Pro nás, kteří se programováním
či konzultacemi okolo technologií živíme může být ale podobná forma správy webu
zajímavou alternativou k serverovým CMS.

Přesně takto vznikl i nový web tkalci.cz. Pelican dokáže obsah zapsaný v
Markdown syntaxi vygenerovat v provázanou kolekci HTLM stránek, kterou byste na
první pohled od Wordpressu nerozpoznali -- jsou zde kategorie, štítky, blog
posty, statické stránky, profilové stránky autorů.


### Ingress

Honza Bednařík nám přichystal jednoznačně nejemotivnější zážitek večera. Ani po
pěti minutách úvodního monologu nikdo z přítomných netušil o čem to vlastně
mluví. "Oukej...", mysleli jsme si, "...asi se nám chystá něco prodat, tablety
nebo nějakou kosmetiku, doba je zlá." To co zprvu připomínalo předváděcí akci s
obědem zdarma se ale nakonec vyvrbilo v představení zajímavé multiplayerové hry.

Ingress se odehrává v reálném prostředí (venku, tam co rostou stromy a svítí
slunko). Potřebujete sice telefon, ale bez fyzické námahy (čti chůze) vám bude k
ničemu. Principem hry je totiž dobývání portálů, které jsou soustředěny kolem
významných míst ve vašem okolí. Rozhodnete se za jakou barvu hrajete (modrá,
zelená), v telefonu si najdete portály a vyrazíte je dobýt. Večer pak zaslouženě
usínáte s mírem v duši, protože jste uchránili důležité kulturní památky před
těmi zlými...

No, a ráno je všechno jinak.

![Ingress v Olomouci](/images/ingress_olomouc.png)

Ingress hrají lidi denně po celém světě už dva roky. Díky němu poznávají
zajímavá místa ve městech. Podobně jako FitBit či Jawbone motivuje hráče k
aktivnějšímu životu. Zkuste.


### PDFMake.org

Ke třetímu pidivýstupu se přímo na místě osmělil Roman Brhel. Krátce a úderně
nám představil další absurditu oživenou javascriptem přímo v prohlížeči.
Tentokrát -- tamtada-tamtada-tamtada-dáááá -- generování PDF!

Fakt. 

Roman potřeboval do svého jazykového softu přidat funkci, která by učitelům
vygenerovala rozvrh hodin ve formě PDFka. Zkoušel různá řešení (serverová),
ale pokaždé s nima bylo moc práce. "Každou, úplně každou čárku v tabulce sem
tam musel explicitně definovat...", plakal Roman.

Protože to je ale chlapec šikovný a umí klást dotazy, narazil na PDFMake, který
jeho problém rázem vyřešil. Jednoduchou syntaxí zadá obsah dokumentu a pak jen
na prvek ve stránce zavěsí akci, která PDF vygeneruje a stáhne do počítače
uživatele.

No uznejte sami, není tohle paráda?

```
var dd = {
	content: [
		'First paragraph',
		'Another paragraph, this time a little bit longer to make sure, 
         this line will be divided into at least two lines'
	]
}
```

*(ukázka popisu dokumentu, který PDFMake přeloží do PDF)*


### Docker dev stack

No, a najednou tu byl poločas a s ním Vojta Orgoň a jeho poctivá přednáška o
vývojovém prostředí postaveného nad Dockerem.

Začala tak, že připojil projektor, otevřel terminál a už z něj neodešel.

Vojta nám na praktických příkladech ukázal, jak řeší obvyklá traumata vývojářů.
Namísto zaplevelení systému knihovnama či variantama jednotlivých programovacích
jazyků využívá Docker. V kontejnerech mu běží databáze, webové servery, aplikace
v Pythonu (různých verzí), Java, Redisy. Každý kontejner má své hřiště, ostatním
se pod nohy neplete, v mateřském systému nevzniká žádný bordel. Protože vše
zapisuje do Dockerfiles, přeinstalace systému je z pohledu devstacku nudná
událost -- na novém počítači stačí zbuildit image a jede se dál.

Pokud se ale začne kontejnerů objevovat víc, a musí se mezi sebou nějak
propojovat, začne být situace nepřehledná. Docker naštěstí kromě samotné
kontejnerizační technologie přichází i se sadou nástrojů, mimo jiné i s tzv.
Composem. Ten dokáže na základě jednoduchého YML zápisu spustit a propojit více
kontejnerů mezi sebou. Rozjetí dev prostředí pak obvykle znamená zavolat příkaz:

```
docker-compose up
```

Pár tipů:

* obvyklé technologie (PostgreSQL, Redis, Python) spouštějte z oficiálních
  images, jejich chod přizpůsobujte překrytím konfiguračních souborů či
  injectnutím custom skriptů
* zapomeňte na Dockeří matru "zbuilděno jednou, provozováno všude" -- produkční
  prostředí obvykle potřebuje kontejner který je co nejmenší a dělá jen to co
  má, při vývoji naopak oceníte podporu v podobě debugovacích nástrojů. Je
  naprosto v pořádku, pokud pro konkrétní službu budete udržovat **několik**
  verzí Dockerfiles. Co prostředí, to jiný popis.
* někdy ani Compose nepomůže... Pak šáhněte po BASH skriptu, Makefile, Pythonu
  či jiné technologii. Zabalte si vaše workflow do další vrstvy, která se
  postará o stažení DB dumpů ze staging serverů, inicializaci prostředí na
  lokálním stroji a na konec i jejich spuštění.


### Dobré jak chleba

Fakt. Syté, chutné, naše. Kdo nebyl, lituje (a my jeho).

**Díky všem co jste přišli a vystupujícím dvojnásob.**

---

*Obrázek Ingressu via [http://droidnet.cz/2013/01/16/co-vam-o-ingressu-mozna-nerekli-2-cast/](http://droidnet.cz/2013/01/16/co-vam-o-ingressu-mozna-nerekli-2-cast/)*
