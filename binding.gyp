{
  "targets": [
    {
      "target_name": "nlapack",
      "sources": [
        "src/index.cc",
        "routines/lineq/matfac/getrf.cc",
        # "routines/lineq/matfac/getrf2.cc",
        "routines/lineq/matfac/gbtrf.cc",
        "routines/lineq/matfac/gttrf.cc",
        # "routines/lineq/matfac/dttrfb.cc",
        "routines/lineq/matfac/potrf.cc",
        # "routines/lineq/matfac/potrf2.cc",
        "routines/lineq/matfac/pstrf.cc",
        "routines/lineq/matfac/pftrf.cc",
        "routines/lineq/matfac/pptrf.cc",
        "routines/lineq/matfac/pbtrf.cc",
        "routines/lineq/matfac/pttrf.cc",
        "routines/lineq/matfac/sytrf.cc",
        # "routines/lineq/matfac/sytrf_aa.cc",
        # "routines/lineq/matfac/sytrf_rook.cc",
        # "routines/lineq/matfac/hetrf.cc",
        # "routines/lineq/matfac/hetrf_aa.cc",
        # "routines/lineq/matfac/hetrf_rook.cc",
        "routines/lineq/matfac/sptrf.cc",

        # "routines/lineq/matfac/hptrf.cc",
        "routines/lineq/solve/getrs.cc",
        "routines/lineq/solve/gbtrs.cc",
        "routines/lineq/solve/gttrs.cc",
        # "routines/lineq/solve/dttrsb.cc",
        "routines/lineq/solve/potrs.cc",
        "routines/lineq/solve/pftrs.cc",
        "routines/lineq/solve/pptrs.cc",
        "routines/lineq/solve/pbtrs.cc",
        "routines/lineq/solve/pttrs.cc",
        "routines/lineq/solve/sytrs.cc",
        # "routines/lineq/solve/sytrs_aa.cc",
        # "routines/lineq/solve/sytrs_rook.cc",
        # "routines/lineq/solve/hetrs.cc",
        # "routines/lineq/solve/hetrs_aa.cc",
        # "routines/lineq/solve/hetrs_rook.cc",
        # "routines/lineq/solve/sytrs2.cc",
        # "routines/lineq/solve/hetrs2.cc",
        "routines/lineq/solve/sptrs.cc",
        # "routines/lineq/solve/hptrs.cc",
        "routines/lineq/solve/trtrs.cc",
        "routines/lineq/solve/tptrs.cc",
        "routines/lineq/solve/tbtrs.cc",

        "routines/lineq/cond/gecon.cc",
        "routines/lineq/cond/gbcon.cc",
        "routines/lineq/cond/gtcon.cc",
        "routines/lineq/cond/pocon.cc",
        "routines/lineq/cond/ppcon.cc",
        "routines/lineq/cond/pbcon.cc",
        "routines/lineq/cond/ptcon.cc",
        "routines/lineq/cond/sycon.cc",
        # "routines/lineq/cond/sycon_rook.cc",
        # "routines/lineq/cond/hecon.cc",
        # "routines/lineq/cond/hecon_rook.cc",
        "routines/lineq/cond/spcon.cc",
        "routines/lineq/cond/trcon.cc",
        "routines/lineq/cond/tpcon.cc",
        "routines/lineq/cond/tbcon.cc",

        "routines/lineq/refine/gerfs.cc",
        "routines/lineq/refine/gerfsx.cc",
        "routines/lineq/refine/gbrfs.cc",
        "routines/lineq/refine/gbrfsx.cc",
        "routines/lineq/refine/gtrfs.cc",
        "routines/lineq/refine/porfs.cc",
        "routines/lineq/refine/porfsx.cc",
        "routines/lineq/refine/pprfs.cc",
        "routines/lineq/refine/pbrfs.cc",
        "routines/lineq/refine/ptrfs.cc",
        "routines/lineq/refine/syrfs.cc",
        "routines/lineq/refine/syrfsx.cc",
        # "routines/lineq/refine/herfs.cc",
        # "routines/lineq/refine/herfsx.cc",
        "routines/lineq/refine/sprfs.cc",
        # "routines/lineq/refine/hprfs.cc",
        "routines/lineq/refine/trrfs.cc",
        "routines/lineq/refine/tprfs.cc",
        "routines/lineq/refine/tbrfs.cc",

        "routines/lineq/matinv/getri.cc",
        "routines/lineq/matinv/potri.cc",
        "routines/lineq/matinv/pftri.cc",
        "routines/lineq/matinv/pptri.cc",
        "routines/lineq/matinv/sytri.cc",
        # "routines/lineq/matinv/sytri_rook.cc",
        # "routines/lineq/matinv/hetri.cc",
        # "routines/lineq/matinv/hetri_rook.cc",
        # "routines/lineq/matinv/sytri2.cc",
        # "routines/lineq/matinv/hetri2.cc",
        # "routines/lineq/matinv/sytri2x.cc",
        # "routines/lineq/matinv/hetri2x.cc",
        "routines/lineq/matinv/sptri.cc",
        # "routines/lineq/matinv/hptri.cc",
        "routines/lineq/matinv/trtri.cc",
        "routines/lineq/matinv/tftri.cc",
        "routines/lineq/matinv/tptri.cc",

        "routines/lineq/mateq/geequ.cc",
        "routines/lineq/mateq/geequb.cc",
        "routines/lineq/mateq/gbequ.cc",
        "routines/lineq/mateq/gbequb.cc",
        "routines/lineq/mateq/poequ.cc",
        "routines/lineq/mateq/poequb.cc",
        "routines/lineq/mateq/ppequ.cc",
        "routines/lineq/mateq/pbequ.cc",
        "routines/lineq/mateq/syequb.cc",
        # "routines/lineq/mateq/heequb.cc",

        "routines/util/ilaver.cc",
        "routines/util/lamch.cc",

        "routines/test/latms.cc"
      ],
      "include_dirs" : [
        "LAPACKE/include",
        "lib"
      ],
      "libraries": [
        "<(module_root_dir)/liblapacke.a",
        "-llapack",
        "-lblas"
      ]
    }
  ]
}
