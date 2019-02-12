from tap_greenhouse.streams.applications import ApplicationsStream
from tap_greenhouse.streams.candidates import CandidatesStream
from tap_greenhouse.streams.jobstages import JobStagesStream
from tap_greenhouse.streams.jobs import JobsStream
from tap_greenhouse.streams.sources import SourcesStream
from tap_greenhouse.streams.eeoc import EEOCStream



STREAMS = [
    ApplicationsStream,
    CandidatesStream,
    JobStagesStream,
    JobsStream,
    SourcesStream,
    EEOCStream,
]
