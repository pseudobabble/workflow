#!/usr/bin/env python3

config = {
    'statuses': ['Due', 'In Progress', 'Overdue', 'Completed'],
    'transition_definitions': [
        {
            'from': 'Due',
            'to': '*'
        },
        {
            'from': 'In Progress',
            'to': 'Overdue'
        },
        {
            'from': 'In Progress',
            'to': 'Completed'
        },
        {
            'from': 'Overdue',
            'to': 'Completed'
        },
        {
            'from': 'Completed',
            'to': 'Due'
        },
    ],
    'location': __file__
}
