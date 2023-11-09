import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2


def hide_labels(v):
    for label in v.subset_labels:
        if label is not None:  # Check to avoid trying to set_text on a NoneType
            label.set_text('')


plt.figure(figsize=(7, 7))
venn = venn2(subsets=(50, 0, 10), set_labels=('NPH', 'P'))
venn.get_label_by_id('B').set_position((0.2, 0.1))
# Hide subset labels (numbers)
hide_labels(venn)

set_sizes = (15, 0, 6, 7, 0, 17, 10)

# Create the Venn diagram
venn = venn3(subsets=set_sizes, set_labels=('EXP', 'NP', 'Savant Cognitive Problems'))
venn.get_label_by_id('A').set_position((0.7, 0))
venn.get_label_by_id('B').set_position((0.0, 0.4))
venn.get_label_by_id('C').set_position((-0.5, 0.1))
hide_labels(venn)

plt.show()

set_sizes = (10, 0, 3, 0, 2, 1, 1)

venn = venn3(subsets=set_sizes, set_labels=('Drawing Sideways Automatically', 'Savant Cognitive Problems', 'NP or P'))
venn.get_label_by_id('A').set_position((0.7, -.3))
venn.get_label_by_id('B').set_position((0.2, 0.3))
venn.get_label_by_id('C').set_position((-0.2, 0.1))
hide_labels(venn)

plt.show()

set_sizes = (4, 5, 0, 8, 4, 3, 2)

venn = venn3(subsets=set_sizes, set_labels=('Drawing Sideways Automatically', 'Savant Cognitive Problems', 'P'))
venn.get_label_by_id('A').set_position((0.9, -0.6))
venn.get_label_by_id('B').set_position((0.1, 0.5))
venn.get_label_by_id('C').set_position((-0.4, 0.4))
hide_labels(venn)

venn = venn2(subsets=(10, 2, 5), set_labels=('NP', "King's Demoness"))
venn.get_label_by_id('A').set_position((-.5, -.4))
venn.get_label_by_id('B').set_position((0.3, 0.1))
# Hide subset labels (numbers)
hide_labels(venn)

plt.show()