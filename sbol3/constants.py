# --------------------------------------------------
# Constants to support SBOL 3
#
# See https://sbolstandard.org/data-model-specification/ for the latest version.
# --------------------------------------------------

SBOL_LOGGER_NAME = 'sbol3'

# ----------
# Namespaces
# ----------

SBOL3_NS = 'http://sbols.org/v3#'
SBOL2_NS = 'http://sbols.org/v2#'
SBOL1_NS = 'http://sbols.org/v1#'

# Provenance
PROV_NS = 'https://www.w3.org/TR/prov-o/'

# Namespace for Chemical Entities of Biological Interest (ChEBI) terms
CHEBI_NS = 'https://identifiers.org/CHEBI:'

# Namespace for Sequence Ontology (SO) terms
SO_NS = "https://identifiers.org/SO:"

# Namespace for Systems Biology Ontology (SBO) terms
SBO_NS = 'https://identifiers.org/SBO:'

# ----------
# SBOL 3 terms
# ----------
SBOL_BUILT = SBOL3_NS + 'built'
SBOL_CARDINALITY = SBOL3_NS + 'cardinality'
SBOL_COLLECTION = SBOL3_NS + 'Collection'
SBOL_COMBINATORIAL_DERIVATION = SBOL3_NS + 'CombinatorialDerivation'
SBOL_COMPONENT = SBOL3_NS + 'Component'
SBOL_COMPONENT_REFERENCE = SBOL3_NS + 'ComponentReference'
SBOL_CONSTRAINT = SBOL3_NS + 'Constraint'
SBOL_CONSTRAINTS = SBOL3_NS + 'hasConstraint'
SBOL_CUT = SBOL3_NS + 'Cut'
SBOL_DESCRIPTION = SBOL3_NS + 'description'
SBOL_DISPLAY_ID = SBOL3_NS + 'displayId'
SBOL_ELEMENTS = SBOL3_NS + 'elements'
SBOL_ENCODING = SBOL3_NS + 'encoding'
SBOL_END = SBOL3_NS + 'end'
SBOL_ENTIRE_SEQUENCE = SBOL3_NS + 'EntireSequence'
SBOL_EXPERIMENT = SBOL3_NS + 'Experiment'
SBOL_FEATURES = SBOL3_NS + 'hasFeature'
SBOL_FRAMEWORK = SBOL3_NS + 'framework'
SBOL_HAS_ATTACHMENT = SBOL3_NS + 'hasAttachment'
SBOL_IMPLEMENTATION = SBOL3_NS + 'Implementation'
SBOL_IN_CHILD_OF = SBOL3_NS + 'inChildOf'
SBOL_INPUT = SBOL3_NS + 'input'
SBOL_INSTANCE_OF = SBOL3_NS + 'instanceOf'
SBOL_INTERACTIONS = SBOL3_NS + 'hasInteraction'
SBOL_INTERACTION = SBOL3_NS + 'Interaction'
SBOL_INTERFACE = SBOL3_NS + 'Interface'
SBOL_INTERFACES = SBOL3_NS + 'hasInterface'
SBOL_LANGUAGE = SBOL3_NS + 'language'
SBOL_LOCATION = SBOL3_NS + 'hasLocation'
SBOL_MODEL = SBOL3_NS + 'Model'
SBOL_MODELS = SBOL3_NS + 'hasModel'
SBOL_NAME = SBOL3_NS + 'name'
SBOL_NAMESPACE = SBOL3_NS + 'Namespace'
SBOL_NON_DIRECTIONAL = SBOL3_NS + 'nondirectional'
SBOL_OBJECT = SBOL3_NS + 'object'
SBOL_ORDER = SBOL3_NS + 'order'
SBOL_ORIENTATION = SBOL3_NS + 'orientation'
SBOL_OUTPUT = SBOL3_NS + 'output'
SBOL_PARTICIPANT = SBOL3_NS + 'participant'
SBOL_PARTCIPATION = SBOL3_NS + 'Participation'
SBOL_PARTICIPATIONS = SBOL3_NS + 'hasParticipation'
SBOL_RANGE = SBOL3_NS + 'Range'
SBOL_RESTRICTION = SBOL3_NS + 'restriction'
SBOL_ROLE = SBOL3_NS + 'role'
SBOL_SEQUENCE = SBOL3_NS + 'Sequence'
SBOL_SOURCE = SBOL3_NS + 'source'
SBOL_SEQUENCES = SBOL3_NS + 'hasSequence'
SBOL_SOURCE_LOCATION = SBOL3_NS + 'sourceLocation'
SBOL_START = SBOL3_NS + 'start'
SBOL_STRATEGY = SBOL3_NS + 'strategy'
SBOL_SUBCOMPONENT = SBOL3_NS + 'SubComponent'
SBOL_SUBJECT = SBOL3_NS + 'subject'
SBOL_TEMPLATE = SBOL3_NS + 'template'
SBOL_TYPE = SBOL3_NS + 'type'
SBOL_VARIABLE = SBOL3_NS + 'variable'
SBOL_VARIABLE_COMPONENT = SBOL3_NS + 'VariableComponent'
SBOL_VARIABLE_COMPONENTS = SBOL3_NS + 'hasVariableComponent'
SBOL_VARIANT = SBOL3_NS + 'variant'
SBOL_VARIANT_COLLECTION = SBOL3_NS + 'variantCollection'
SBOL_VARIANT_DERIVATION = SBOL3_NS + 'variantDerivation'

# Valid values for Feature orientation
# See SBOL3 Section 6.4.1 Table 5
SBOL_INLINE = SBOL3_NS + 'inline'
SBOL_REVERSE_COMPLEMENT = SBOL3_NS + 'reverseComplement'

# Valid values for Combinatorial Derivation strategy
# See SBOL3 Section 6.5 Table 12
SBOL_ENUMERATE = SBOL3_NS + 'enumerate'
SBOL_SAMPLE = SBOL3_NS + 'sample'

# Valid values for Variable Component cardinality
# See SBOL3 Section 6.5 Table 13
SBOL_ONE = SBOL3_NS + 'one'
SBOL_ONE_OR_MORE = SBOL3_NS + 'oneOrMore'
SBOL_ZERO_OR_MORE = SBOL3_NS + 'zeroOrMore'
SBOL_ZERO_OR_ONE = SBOL3_NS + 'zeroOrOne'

# A namespace for internal URIs and for testing
PYSBOL3_NS = 'https://github.com/synbiodex/pysbol3#'
PYSBOL3_MISSING = PYSBOL3_NS + 'missing'


# ----------
# Provenance terms
# ----------
PROV_DERIVED_FROM = PROV_NS + 'wasDerivedFrom'
PROV_GENERATED_BY = PROV_NS + 'wasGeneratedBy'


# ----------
# Component/Feature roles
#
# * These are common, others can be used as well.
# * See the SBOL 3 spec, Section 6.4, Table 4
# ----------
SO_PROMOTER = SO_NS + "0000167"
SO_RBS = SO_NS + "0000139"
SO_CDS = SO_NS + "0000316"
SO_TERMINATOR = SO_NS + "0000141"
SO_GENE = SO_NS + "0000704"
SO_OPERATOR = SO_NS + "0000057"
SO_ENGINEERED_GENE = SO_NS + "0000280"
SO_MRNA = SO_NS + "0000234"
CHEBI_EFFECTOR = CHEBI_NS + '35224'
SO_TRANSCRIPTION_FACTOR = SO_NS + "0003700"

# Component types
# See the SBOL 3 spec, Section 6.4, Table 2
SBO_DNA = SBO_NS + '0000251'
SBO_RNA = SBO_NS + '0000250'
SBO_PROTEIN = SBO_NS + '0000252'
SBO_SIMPLE_CHEMICAL = SBO_NS + '0000247'
SBO_NON_COVALENT_COMPLEX = SBO_NS + '0000253'
SBO_FUNCTIONAL_ENTITY = SBO_NS + '0000241'

# Component types
# See the SBOL 3 spec, Section 6.4, Table 3
SO_LINEAR = SO_NS + "0000987"
SO_CIRCULAR = SO_NS + "0000988"
SO_SINGLE_STRANDED = SO_NS + "0000984"
SO_DOUBLE_STRANDED = SO_NS + "0000985"

# RECOMMENDED URIs for expressing identity and orientation with
# the restriction property.
# See the SBOL 3 spec, Section 6.4, Table 7
SBOL_VERIFY_IDENTICAL = SBOL3_NS + 'verifyIdentical'
SBOL_DIFFERENT_FROM = SBOL3_NS + 'differentFrom'
SBOL_REPLACES = SBOL3_NS + 'replaces'
SBOL_SAME_ORIENTATION_AS = SBOL3_NS + 'sameOrientationAs'
SBOL_OPPOSITE_ORIENTATION_AS = SBOL3_NS + 'oppositeOrientationAs'

# RECOMMENDED URIs for expressing topological relations with
# the restriction property.
# See the SBOL 3 spec, Section 6.4, Table 8
SBOL_IS_DISJOINT_FROM = SBOL3_NS + 'isDisjointFrom'
SBOL_STRICTLY_CONTAINS = SBOL3_NS + 'strictlyContains'
SBOL_CONTAINS = SBOL3_NS + 'contains'
SBOL_EQUALS = SBOL3_NS + 'equals'
SBOL_MEETS = SBOL3_NS + 'meets'
SBOL_COVERS = SBOL3_NS + 'covers'
SBOL_OVERLAPS = SBOL3_NS + 'overlaps'

# RECOMMENDED URIs for expressing sequential relations with the
# restriction property
# See the SBOL 3 spec, Section 6.4, Table 9
SBOL_PRECEDES = SBOL3_NS + 'precedes'
SBOL_STRICTLY_PRECEDES = SBOL3_NS + 'strictlyPrecedes'
# SBOL_MEETS = SBOL3_NS + 'meets'
# SBOL_OVERLAPS = SBOL3_NS + 'overlaps'
# SBOL_CONTAINS = SBOL3_NS + 'contains'
# SBOL_STRICTLY_CONTAINS = SBOL3_NS + 'strictlyContains'
# SBOL_EQUALS = SBOL3_NS + 'equals'
SBOL_FINISHES = SBOL3_NS + 'finishes'
SBOL_STARTS = SBOL3_NS + 'starts'

# Interaction types
# See the SBOL 3 spec, Section 6.4, Table 10
SBO_INHIBITION = SBO_NS + '0000169'
SBO_STIMULATION = SBO_NS + '0000170'
SBO_BIOCHEMICAL_REACTION = SBO_NS + '0000176'
SBO_NON_COVALENT_BINDING = SBO_NS + '0000177'
SBO_DEGRADATION = SBO_NS + '0000179'
SBO_GENETIC_PRODUCTION = SBO_NS + '0000589'
SBO_CONTROL = SBO_NS + '0000168'

# Participation roles
# See the SBOL 3 spec, Section 6.4, Table 11
SBO_INHIBITOR = SBO_NS + '0000020'
SBO_INHIBITED = SBO_NS + '0000642'
SBO_STIMULATOR = SBO_NS + '0000459'
SBO_STIMULATED = SBO_NS + '0000643'
SBO_REACTANT = SBO_NS + '0000010'
SBO_PRODUCT = SBO_NS + '0000011'
SBO_PROMOTER = SBO_NS + '0000598'
SBO_MODIFIER = SBO_NS + '0000019'
SBO_MODIFIED = SBO_NS + '0000644'
SBO_TEMPLATE = SBO_NS + '0000645'

# RDF File Formats
NTRIPLES = 'nt'
RDF_XML = 'xml'
TURTLE = 'ttl'
JSONLD = 'jsonld'
SORTED_NTRIPLES = 'sorted nt'
