Title: Readme

Web [tkalci.cz](http://tkalci.cz) je generován nástrojem [Pelican](), který
konvertuje obsah sepsaný v Markdown syntaxi na kolekci statických stránek. 


## Obsah

Vše důležité je uloženo ve složce `content/`:

* `blog/pozvanky/` -- Sem budeme ukládat pozvánky na naše srazy. V zářné
  budoucnosti pak některá dobrá duše napíše kód, který její obsah automaticky
  překlopí na služby [srazy.info](http://srazy.info/tkalci-na-webu) a 
  [lanyrd.com](http://lanyrd.com/series/tkalci-na-webu/). Než se tak opravdu stane, budem
  tam obsah pozvánky manuálně kopírovat.
* `blog/zapisy/` -- Vystavení videí ze srazu vždycky chvíli trvá a ne každý si
  najde 3 hodiny na jejich zpětné shlédnutí. Proto budeme ze srazů pořizovat i
  stručný textový zápis, jehož autorem může být kdokoli z přítomných. Zápis
  by měl být stručným představením toho, co na srazu zaznělo, ideálně doplněno
  o relevantní odkazy, slajdy a posléze i videa.
* `stranky/` -- Víceméně statický obsah webu do kterého nebude potřeba příliš
  často zasahovat.

Podrobnosti k jednotlivým typům obsahu následují.


### Formát souborů

Obsah webu je vytvářen ze souborů, které musí:

* být uloženy v konkrétních adresářích
* být pojmenovány podle předem dané formy
* být sepsány v [Markdown]() syntaxi doplněné sadou metadat 

Každý soubor je rozdělen na 2 části: metadata v úvodu a samotný obsah. Např.:

    Title: Nádherný titulek
    Date: 2015-09-19 08:23

    První obsahový odstavec.

    Druhý obsahový odstavec.

Metadata v úvodu, podle kterých *Pelican* pozná kam obsah zařadit, jakou
šablonu použít, apod., mají formu `Klic: Hodnota`. *Pelican* definuje sadu
[standardních klíčů](), tkalcovská implementace pak přidává pár nových (popsáno
níže).


### Pozvánky

Kam pozvánky ukládat:

    content/blog/pozvanky/<cislo>_<jmeno>.md

`<cislo>` je pořadové číslo srazu, `<jmeno>` je titulek srazu přepsaný do malých
písmen bez diakritiky, mezery nahrazeny za znak `_`.

Metadata:

    Title: Název srazu
    Date: Datum konání srazu, např. 2015-06-09 18:00
    Tags: Tagy vyjadřující témata srazu, např. expressjs, nodejs
    Summary: Jednovětný popis srazu


### Zápisy

Kam zápisy ukládat:

    content/blog/zapisy/<cislo>_<jmeno>.md

`<cislo>` je pořadové číslo srazu, `<jmeno>` je titulek srazu přepsaný do malých
písmen bez diakritiky, mezery nahrazeny za znak `_`.

Metadata:

    Title: Název srazu
    Date: Datum konání srazu, např. 2015-06-09 18:00
    Tags: Tagy vyjadřující témata srazu, např. expressjs, nodejs
    Authors: Jméno autora (toho, kdo zápis vytváří)
    Summary: Jednovětný popis srazu

Metadata jsou shodná s těmi, která jsou uvedena u pozvánky. Nově se zde vyskytuje
pouze klíč `Authors`, do kterého je možné uložit jména lidí (oddělena čárkami), 
kteří zápis pořídili. *Pelican* pak umí automaticky pro každého člověka vytvořit
profilovou stránku se seznamem obsahu, které dotyčný na web vystavil.


### Statické stránky

Kam stránky ukládat:

    content/stranky/<jmeno>.md

Metadata:

    Title: Jméno stránky
    Summary: Jednovětný popis stránky.
    Tags: Tagy vyjadřující obsah stránky, např. books
    Template: Jméno šablony, nepovinný parametr
    FrontImage: Cesta k úvodnímu obrázku, nepovinný parametr

Význam jednotlivých klíčů je podobný jako u zápisů či pozvánek. Za komentář stojí:

* `Template` -- každá stránka se generuje prostřednictvím některé ze šablon
  z adresáře `templates/templates/`. Defaultně si *Pelican* šáhne po šabloně `page`,
  ale právě s pomocí klíče `Template` je možné tuto volbu přebít.
* `FrontImage` -- každá ze stránek může být uvozena obrázkem roztaženým přes
  celou šířku stránky. Stačí do tohoto klíče uložit cestu k obrázku z adresáře
  `image`, např. `FrontImage: /images/img03.jpg`

Většina stránek má statický charakter, a nebude vznikat velká potřeba jejich 
obsah často měnit. Vyjímkou je soubor `content/blog/knihovna.md`, ve kterém
udržujeme seznam sdílených knih a lidí, kteří si některou z nich půjčili.  


### Obrázky

Do složky `content/images/` je možné ukládat obrázky, na které se pak dá odkazovat
z obsahových Markdown souborů (např. prostřednictvím meta klíče `FrontImage` nebo
standardně [Markdown syntaxí pro obrázky]()).

Cesta k obrázku se zadává ve tvaru `/images/<jmeno>`.


## Jak můžete pomoct

1. Udržovat aktuální obsah
2. Rozšiřovat funkcionalitu *Pelicana* nebo vytvořit podpůrné skripty


### Úpravy obsahu

Jsme na [GitHubu](), obsah tkalcovského webu je přístupný komukoli. Pokud naleznete
nějakou nepřesnost, budete chtít pořídit zápis s uskutečněného srazu, aktualizovat
informace v knihovně, či upravit/přidat obsah jakékoliv stránky, směle do toho!

Stačí když pošlete pull request s vaší úpravou.


### Rozšiřování funkcionality

Stránky v současném stavu (září 2015) zdaleka nejsou v podobě, ve které by mohly
být. K dokonalosti jim chybí spousta detailů, přičemž část z nich je možné vyřešit
doprogramováním filtrů pro šablonový systém Jinja nebo rozšířením Markdown syntaxe.
Pokud budete mít čas a chuť některou z následujících věcí pořešit, [ozvěte se]().


#### Bohatší formátování obrázků v obsahu

Obrázky v Markdown syntaxi se standardně vkládají formou `![alt](cesta)`.
Je třeba napsat rozšíření pro Markdown, které bude umět vložit do stránky jednu
ze tří variant obrázku:

1. velký obrázek zarovnaný na střed stránky, `![|alt](cesta)`
2. menší obrázek zarovnaný nalevo, `![<alt](cesta)`
3. menší obrázek zarovnaný napravo, `![>alt](cesta)`

(to o jakou variantu jde vyjadřuje první znak v alt popisku).

HTML kód:

Varianta 1 (zarovnání na střed):

    <figure class="sp-image-center">
        <img src="{{ cesta }}" alt="{{ alt_popisek }}">
        <figcaption class="sp-caption">{{ alt_popisek }}</figcaption>
    </figure>

Varianta 2 (zarovnání vlevo):

    <figure class="sp-image-left">
        <img src="{{ cesta }}" alt="{{ alt_popisek }}">
        <figcaption class="sp-caption">{{ alt_popisek }}</figcaption>
    </figure>

Varianta 3 (zarovnání vpravo):

    <figure class="sp-image-right">
        <img src="{{ cesta }}" alt="{{ alt_popisek }}">
        <figcaption class="sp-caption">{{ alt_popisek }}</figcaption>
    </figure>

Všechny tři varianty musí počítat s tím, že popisek nemusí být zadán (buď bude
úplně prázdný, nebo bude obsahovat jen formátovací značku `<`, `|` nebo `>`).
V tomto případě není nutné generovat obsah `<figcaption>`.

Obrázky se vkládají mezi odstavce, např.:

    <p>První odstavec</p>
    <figure>...</figure>
    <p>První odstavec</p>


#### Citace
  
Podobně jako u obrázků je možné do obsahu vkládat i pěkně naformátované citace:

1. velká zarovnaná na střed stránky, `> |citace`
2. menší zarovnaná nalevo, `> <citace`

To o jakou citaci jde určuje první znak jejího obsahu.

HTML kód:

Varianta 1 (zarovnání na střed):

    <blockquote class="sp-quote">Obsah citace</blockquote>

Varianta 2 (zarovnání nalevo):

    <blockquote class="sp-quote sp-left">Obsah citace</blockquote>

Citace se vkládají mezi odstavce, např.:

    <p>První odstavec</p>
    <blockquote>...</blockquote>
    <p>První odstavec</p>

(v případě nalevo zarovnané citace je bude její obsah vložen na levou stranu
následujícího odstavce)


#### Ozdobná kapitálka v prvním odstavci

Jinja filtr, který nahradí první písmeno v prvním odstavci za HTML strukturu:

    <span class="sp-dropcap">PISMENO</span>

Příklad:

    Před úpravou:
    <p>Toto je první odstavec.</p>
    <p>Toto je druhý odstavec.</p>

    Po úpravě:
    <p><span class="sp-dropcap">T</span>oto je první odstavec.</p>
    <p>Toto je druhý odstavec.</p>


#### Vkládání videí do obsahu

Pro *Pelican* existuje plugin, s jehož pomocí se dá do RST obsahu vložit video z
YouTube. Pro obsah psaný Markdown syntaxí jsem ale nic podobného nenašel. 

Potřebujeme vymyslet syntaxi a zrealizovat rozšíření pro Markdown pro vkládání
videí do stránek.


#### Vkládání slajdů do obsahu

Podobná situace jako u videí se opakuje i u slajdů. Z většiny výstupů sice 
slajdy máme, jejich forma je ale velmi pestrá (PDF, HTML, GDocs). 

Potřebujeme najít služb, do které nalijeme všechny slajdy co máme uploadnuté
na webu tkalci.cz. Z ní pak chceme umět vkládat interaktivní slajdy do stránek
a to v Markdown syntaxi.
