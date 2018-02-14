import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 90),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# c-style (loops)
high_measurements1 = []
count = len(measurements)
index = 0
while index < count:
    m = measurements[index]
    if m.value >= 70:
        high_measurements1.append(m)

    index += 1

print(high_measurements1)

# in python it should look like this, but it's still loop...
high_measurements_1 = []
for m in measurements:
    if m.value >= 70:
        high_measurements_1.append(m.value)

print(high_measurements_1)

# list of high values via comprehension
high_measurements2 = [
    m.value
    for m in measurements
    if m.value >= 70
]
print(high_measurements2)

# via generator expression
high_m_gen = (
    m.value
    for m in measurements
    if m.value >= 70
)
print(high_m_gen)

high_measurements3 = list(high_m_gen)  # process the generator to get something printable

print(high_measurements3)

# high value dict via comprehension

high_m_by_id = {
    m.id: m
    for m in measurements
    if m.value >= 70
}
print(high_m_by_id)

# high value distinct via set
high_values_distinct = {
    m.value
    for m in measurements
    if m.value >= 70
}
print(high_values_distinct)