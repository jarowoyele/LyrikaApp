import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from split import unique 
from azlyrics.azlyrics import lyrics
# from streamlit.proto.TextArea_pb2 import TextArea


    

def main():
    st.title("Lyrica")
    
    
    def searchlyrics():
        song = lyrics(Artist_name, Song_name)
        for words in song:
            return (words)

    def parse_lyrics():
        profane_words = "4r5e5h1t,fuck,bustin\',busting,fucked,5hit,a55,anal,anus,ar5e,arrse,arse,ass,ass-fucker,asses,assfucker,assfukka,asshole,assholes,asswhole,a_s_s,b!tch,b00bs,b17ch,b1tch,ballbag,balls,ballsack,bastard,beastial,beastiality,bellend,bestial,bestiality,bi+ch,biatch,bitch,bitcher,bitchers,bitches,bitchin,bitching,bloody,blow job,blowjob,blowjobs,boiolas,bollock,bollok,boner,boob,boobs,booobs,boooobs,booooobs,booooooobs,breasts,buceta,bugger,bum,bunny fucker,butt,butthole,buttmuch,buttplug,c0ck,c0cksucker,carpet muncher,cawk,chinkcipa,cl1t,clit,clitoris,clits,cnut,cock,cock-sucker,cockface,cockhead,cockmunch,cockmuncher,cocks,cocksuck, cocksucked, cocksucker,cocksucking,cocksucks,cocksuka,cocksukka,cok,cokmuncher,coksucka,coon,cox,crap,cum,cummer,cumming,cums,cumshot,cunilingus,cunillingus,cunnilingus,cunt,cuntlick, cuntlicker, cuntlicking, cunts,cyalis,cyberfuc,cyberfuck, cyberfucked, cyberfucker,cyberfuckerscyberfucking,d1ck,damn,dick,dickhead,dildo,dildos,dink,dinks,dirsa,dlck,dog-fucker,doggin,dogging,donkeyribber,doosh,duche,dyke,ejaculate,ejaculated,ejaculates,ejaculating, ejaculatings,ejaculation,ejakulate,f u c k,f u c k e r,f4nny,fag,fagging,faggitt,faggot,faggs,fagot,fagots,fags,fanny,fannyflaps,fannyfucker,fanyy,fatass,fcuk,fcuker,fcuking,feck,fecker,felching,fellate,fellatio,fingerfuck, fingerfucked, fingerfucker,fingerfuckers,fingerfucking,fingerfucks,fistfuck,fistfucked, fistfucker,fistfuckers, fistfucking, fistfuckings, fistfucks, flangefook,fookefuck,fucka,fucked,fucker,fuckers,fuckhead,fuckheads,fuckin,fucking,fuckings,fuckingshitmotherfucker,fuckme, fucks,fuckwhit,fuckwit,fudge packer,fudgepacker,fuk,fukerfukker,fukkin,fuks,fukwhit,fukwit,fux,fux0r,f_u_c_k,gangbang,gangbanged, gangbangs, gaylord,gaysex,goatse,God,god-dam,god-damned,goddamn,goddamned,hardcoresex, hell,heshe,hoar,hoare,hoer,homo,hore,horniest,horny,hotsex,jack-off, jackoff,jap,jerk-off, jism,jiz,jizm, jizz,kawk,knob,knobeadknobed,knobend,knobhead,knobjocky,knobjokey,kock,kondum,kondums,kum,kummer,kumming,kums,kunilingus,l3i+ch,l3itch,labia,lmfao,lust,lusting,m0f0,m0fo,m45terbate,ma5terb8,ma5terbate,masochist,master-bate,masterb8,masterbat*,masterbat3,masterbate,masterbation,masterbations,masturbate,mo-fo,mof0,mofo,mothafuck,mothafucka,mothafuckas,mothafuckaz,mothafucked, mothafucker,mothafuckers,mothafuckin,mothafucking, mothafuckings,mothafucks,mother fucker,motherfuck,motherfucked,motherfucker,motherfuckers,motherfuckin,motherfucking,motherfuckings,motherfuckka,motherfucks,muff,mutha,muthafecker,muthafuckker,muther,mutherfucker,n1gga,n1gger,nazi,nigg3r,nigg4h,nigga,niggah,niggas,niggaz,nigger,niggers, nob,nob jokey,nobhead,nobjocky,nobjokey,numbnuts,nutsack,orgasim,orgasims, orgasm,orgasms, p0rn,pawn,pecker,penis,penisfucker,phonesex,phuck,phuk,phuked,phuking,phukked,phukking,phuks,phuq,pigfucker,pimpis,piss,pissed,pisser,pissers,pisses,pissflaps,pissin, pissing,pissoff,poop,porn,porno,pornography,pornos,prick,pricks, pron,pube,pusse,pussi,pussies,pussy,pussys, rectum,retard,rimjaw,rimming,s hit,s.o.b.,sadist,schlong,screwing,scroat,scrote,scrotum,semen,sex,sh!+,sh!t,sh1tshag,shagger,shaggin,shagging,shemale,shi+,shit,shitdick,shite,shited,shitey,shitfuck,shitfull,shithead,shiting,shitings,shits,shitted,shitter,shitters, shitting,shittings,shitty,skank,slut,sluts,smegma,smut,snatch,son-of-a-bitch,spac,spunk,s_h_i_t,t1tt1e5,t1tties,teets,teez,testical,testicle,tit,titfuck,tits,titt,tittie5,tittiefucker,titties,tittyfuck,tittywank,titwank,tosser,turd,tw4t,twat,twathead,twatty,twunt,twunter,v14gra,v1gra,vagina,viagra,vulva,w00se,wang,wank,wanker,wanky,whoar,whore,willies,willy,xrated,xxx"
        profane = profane_words.replace(",", " ")
        profane = profane.split(" ")
        profane = unique.union(set(profane))
        stpwrds = stopwords.words("english")
        tokens = word_tokenize(searchlyrics())
        removing_stopwords = [words for words in tokens if not words in stpwrds]
        new_stopwords = stopwords.words("english")
        new_stopwords = new_stopwords.extend(profane)
        removing = [word for word in removing_stopwords if word in profane]
        return removing

    

 
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Forms Tutorial")
        with st.form(key = "searcher"):
            Artist_name = st.text_input("Artist")
            Song_name = st.text_input("Song")
            Fetch = st.form_submit_button("Fetch Lyrics")

            if Fetch:
                    with st.beta_expander("Lyrics"):
                         st.write(searchlyrics())
                    st.success("Lyrics fetched successfully") 
                    
           
        with st.form(key="form1"):
            # Lyrics = st.text_area("Lyrics", height=300)
            lyrica = st.empty()
            Analyze = st.form_submit_button("Analyze")

            if Analyze:
                with st.beta_expander("Keywords"): 
                     st.write(parse_lyrics())
          
    
    else:
        st.subheader("About")




if __name__ == "__main__":
    main()