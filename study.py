import tkinter as tk

class LatinTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Latin Study Tool")

        self.latin_text = tk.Text(root, height=20, wrap='word', padx=10, pady=10, font=('Arial', 14))
        self.latin_text.pack(expand=1, fill='both')

        # We set the wraplength property to ensure the text will wrap and not expand the window
        self.translation_label = tk.Label(
            root, text='', relief="solid", wraplength=500, padx=10, pady=10, height=6, anchor='nw', justify='left', bg='darkred'
            , font=('Arial', 14))
        self.translation_label.pack(expand=0, fill='x')

        self.latin_text.bind('<ButtonRelease-1>', self.show_translation)

        # Full text of Caesar IV 24-29 broken into sentences and phrases
        self.latin_phrases = [
            {"latin": "at barbari, consilio Romanorum cognito praemisso equitatu et essedariis, quo plerumque genere in proeliis uti consuerunt, reliquis copiis subsecuti nostros navibus egredi prohibebant.",
             "english": "But the barbarians, knowing the plan of the Romans, sent ahead cavalry and charioteers, which type they generally use in battles, and followed with the rest of their forces to prevent our men from disembarking from the ships."},
            {"latin": "erat ob has causas summa difficultas, quod naves propter magnitudinem nisi in alto constitui non poterant;",
             "english": "There was the greatest difficulty for these reasons, because the ships on account of their size could not stop except in deep water;"},
            {"latin": "militibus autem, ignotis locis, impeditis manibus, magno et gravi onere armorum oppressis simul et de navibus desiliendum et in fluctibus consistendum et cum hostibus erat pugnandum.",
             "english": "The soldiers, in unknown places, with their hands impeded, weighed down by the heavy and burdensome load of weapons, had at the same time to jump down from the ships, stand in the waves, and fight with the enemy."},
            {"latin": "cum illi aut ex arido aut paulum in aquam progressi omnibus membris expediti notissimis locis, audacter tela coicerent et equos insuefactos incitarent.",
             "english": "While they, either from dry land or having advanced a little into the water, with all limbs unencumbered, in very well-known places, boldly threw weapons and spurred on their horses accustomed to this kind of action."},
            {"latin": "quibus rebus nostri perterriti atque huius omnino generis pugnae imperiti non eadem alacritate ac studio quo in pedestribus uti proeliis consuerant utebantur.",
             "english": "Terrified by these things and entirely unskilled in this kind of fighting, our men did not use the same zeal and eagerness which they had been accustomed to use in foot battles."},
            {"latin": "quod ubi Caesar animadvertit, naves longas, quarum et species erat barbaris inusitatior et motus ad usum expeditior, paulum removeri ab onerariis navibus et remis incitari et ad latus apertum hostium constitui atque inde fundis, sagittis, tormentis hostes propelli ac submoveri iussit;",
             "english": "When Caesar noticed this, he ordered the long ships, whose appearance was unusual to the barbarians and whose movement was more unimpeded for use, to be moved a little away from the transport ships and to be propelled by oars and stationed towards the open flank of the enemy, and from there to be driven against the enemy and moved back with slings, arrows, and engines;"},
            {"latin": "quae res magno usui nostris fuit.",
             "english": "This arrangement was of great service to our men."},
            {"latin": "nam et navium figura et remorum motu et inusitato genere tormentorum permoti barbari constiterunt ac paulum modo pedem rettulerunt.",
             "english": "For the barbarians, disturbed by the shape of the ships, the movement of the oars, and the unusual type of engines, stopped and retreated a little."},
            {"latin": "atque nostris militibus cunctantibus, maxime propter altitudinem maris, qui decimae legionis aquilam ferebat, contestatus deos, ut ea res legioni feliciter eveniret, 'desilite', inquit, 'milites, nisi vultis aquilam hostibus prodere; ego certe meum rei publicae atque imperatori officium praestitero.'",
             "english": "And while our soldiers hesitated, especially on account of the depth of the sea, he who carried the eagle of the tenth legion, having implored the gods that this circumstance might turn out favorably for the legion, exclaimed, 'Jump down, soldiers, unless you want to betray the eagle to the enemy; I certainly shall have done my duty to the republic and my commander.'"},
            {"latin": "tum nostri, cohortati inter se, ne tantum dedecus admitteretur, universi ex navi desiluerunt.",
             "english": "Then our soldiers, having encouraged one another not to allow so great a disgrace, all leaped from the ship together."},
            {"latin": "hos item ex proximis primi navibus cum conspexissent, subsecuti hostibus adpropinquaverunt.",
             "english": "When those in the nearest ships likewise saw these, they followed them closely and approached the enemy."},
            {"latin": "pugnatum est ab utrisque acriter.",
             "english": "The fight was maintained vigorously on both sides."},
            {"latin": "nostri tamen, quod neque ordines servare neque firmiter insistere poterant neque signa subsequi, atque alius alia ex navi quibuscumque signis occurrerat se adgregabat, magnopere perturbabantur;",
             "english": "Our men, however, because they could neither keep their ranks, nor get firm footing, nor follow their standards, and one from one ship, another from another, assembled around whatever standards they met, were generally in great disorder;"},
            {"latin": "hostes vero, notis omnibus vadii, ubi ex litore aliquos singularis ex navi egredientes conspexerant, incitatis equis impeditos adoriebantur, plures paucos circumsistebant, alii ab latere aperto in universos tela coniciebant.",
             "english": "while the enemy, acquainted with all the shallows, when from the shore they saw any coming from the ships one by one, urged on their horses and attacked the impeded men, many surrounded a few, others threw their weapons upon the whole mass of our men, on their exposed flank."},
            {"latin": "quod ubi Caesar animadvertit, naves longas, quarum et species erat barbaris inusitatior et motus ad usum expeditior, paulum removeri ab onerariis navibus et remis incitari et ad latus apertum hostium constitui atque inde fundis, sagittis, tormentis hostes propelli ac submoveri iussit;",
             "english": "When Caesar observed this, he ordered the boats of the ships of war and the scout boats to be filled with soldiers, and sent them to assist those whom he had observed in distress."},
            {"latin": "nostri simul in arido constiterunt, suis omnibus consecutis, in hostes impetum fecerunt atque eos in fugam dederunt; neque longius prosequi potuerunt, quod equites cursum tenere atque insulam capere non potuerant. hoc unum ad pristinam fortunam Caesar defuit.",
             "english": "Our men, as soon as they made good their footing on dry ground, and all their comrades had joined them, made an attack upon the enemy, and put them to flight, but could not pursue them very far, because the horse had not been able to maintain their course at sea and reach the island. This alone was wanting to Caesar's accustomed success."},
            {"latin": "hostes proelio superati, simul atque se ex fuga receperunt, statim ad Caesarem legatos de pace miserunt; obsides daturos quaeque imperasset sese facturos polliciti sunt.",
             "english": "The enemy being thus vanquished in battle, as soon as they recovered after their flight, instantly sent embassadors to Caesar to negotiate about peace. They promised to give hostages and perform what he should command."},
            {"latin": "una cum his legatis Commius Atrebas venit, quem supra demonstraveram a Caesare in Britanniam praemissum.",
             "english": "Together with these embassadors came Commius the Atrebation, who, as I have above said, had been sent by Caesar into Britain."},
            {"latin": "hunc illi e navi egressum, cum ad eos oratoris modo Caesaris mandata deferret, comprehenderant atque in vincula coniecerant; tum proelio facto remiserunt.",
             "english": "Him they had seized upon when leaving his ship, although in the character of embassador he bore the general's commission to them, and thrown into chains: then after the battle was fought, they sent him back."},
            {"latin": "in petenda pace eius rei culpam in multitudinem contulerunt et propter imprudentiam ut ignosceretur petiverunt.",
             "english": "In suing for peace cast the blame of that act upon the common people, and entreated that it might be pardoned on account of their indiscretion."},
            {"latin": "Caesar, questus quod, cum ultro in continentem legatis missis pacem ab se petissent, bellum sine causa intulissent, ignoscere imprudentiae dixit obsidesque imperavit.",
             "english": "Caesar, complaining, that after they had sued for peace, and had voluntarily sent embassadors into the continent for that purpose, they had made war without a reason, said that he would pardon their indiscretion, and imposed hostages."},
            {"latin": "quorum illi partem statim dederunt, partem ex longinquioribus locis arcessitam paucis diebus sese daturos dixerunt.",
             "english": "A part of whom they gave immediately; the rest they said they would give in a few days, since they were sent for from remote places."},
            {"latin": "interea suos omnes in agros remigrare iusserunt, principesque undique convenire et se civitatesque suas Caesari commendare coeperunt.",
             "english": "In the meantime they ordered their people to return to the country parts, and the chiefs assembled from all quarters, and proceeded to surrender themselves and their states to Caesar."},
            {"latin": "his rebus pace confirmata, post diem quartum quam est in Britanniam ventum naves XVIII de quibus supra demonstratum est, quae equites sustulerant, ex superiore portu leni vento solverunt.",
             "english": "A peace being established by these proceedings four days after we had come into Britain, the eighteen ships, to which reference has been made above, and which conveyed the cavalry, set sail from the upper port with a gentle gale."},
            {"latin": "quae cum adpropinquarent Britanniae et ex castris viderentur, tanta tempestas subito coorta est ut nulla earum cursum tenere posset, sed aliae eodem unde erant profectae referrentur, aliae ad inferiorem partem insulae, quae est propius solis occasum, magno suo cum periculo deicerentur; quae tamen ancoris iactis cum fluctibus complerentur, necessario adversa nocte in altum provectae continentem petierunt.",
             "english": "When they were approaching Britain and were seen from the camp, so great a storm suddenly arose that none of them could maintain their course at sea; some were taken back to the same port from which they had started; others, to their great danger, were driven to the lower part of the island, nearer to the west; having cast anchor as they were getting filled with water, they set out for the continent out of necessity during a stormy night."},
        ]

        # Add the Latin text to the Text widget
        for paragraph in self.latin_phrases:
            self.latin_text.insert(tk.END, f"{paragraph['latin']}\n\n")

    def show_translation(self, event=None):
        try:
            selected_text = self.latin_text.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            translation = self._find_translation(selected_text)
            self.translation_label['text'] = translation if translation else ''
        except tk.TclError:
            self.translation_label['text'] = ''

    def _find_translation(self, selected_text):
        # Check if the selected text is part of any phrase
        for paragraph in self.latin_phrases:
            if selected_text in paragraph['latin']:
                return paragraph['english']
        return ''

if __name__ == "__main__":
    root = tk.Tk()
    app = LatinTranslator(root)
    root.mainloop()